import streamlit as st
from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt
from py2neo import Graph
from langchain_community.vectorstores.neo4j_vector import remove_lucene_chars
from typing import List
import json
from google.generativeai import GenerativeModel, configure
import os
from dotenv import load_dotenv
load_dotenv()

# Neo4j connection details
NEO4J_URI="neo4j+s://ae618189.databases.neo4j.io"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="apTUdkOHHfIvxt2jZkDnvTKePpBevU0ZQjINCda62Rs"



# Function to connect to Neo4j
def connect_to_neo4j():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))


# Connect to Neo4j
graph = Graph(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# Configure Google Generative AI
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')
model = GenerativeModel(model_name="gemini-1.5-flash-latest")


def extract_entities(question: str) -> List[str]:
    prompt = f"""
    Extract diseases, symptoms, causes, risk factors, overview and treatment entities from the following text. 
    Return the result as a JSON array of strings.

    Text: {question}

    JSON Result:
    """

    response = model.generate_content(prompt)
    
    try:
        content = response.text
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        entities = json.loads(content)
        return entities if isinstance(entities, list) else []
    except json.JSONDecodeError:
        print(f"Failed to parse JSON from response: {response.text}")
        return []

def structured_retriever(question: str) -> str:
    result = ""
    entities = extract_entities(question)
    print(entities)
    for entity in entities:
        response = graph.run(
            """
            MATCH (n)
            WHERE n.name =~ $entity_regex
            WITH n
            OPTIONAL MATCH (n)-[r]->(m)
            RETURN n.name + ' - ' + type(r) + ' -> ' + m.name AS output
            UNION
            MATCH (n)
            WHERE n.name =~ $entity_regex
            WITH n
            OPTIONAL MATCH (n)<-[r]-(m)
            RETURN m.name + ' - ' + type(r) + ' -> ' + n.name AS output
            LIMIT 50
            """,
            entity_regex=f"(?i).*{entity}.*"
        )
        result += "\n".join([record["output"] for record in response if record["output"] is not None])
    return result

def create_graph_from_result(result: str) -> nx.Graph:
    G = nx.Graph()
    for line in result.split('\n'):
        if ' - ' in line and ' -> ' in line:
            source, rel_target = line.split(' - ')
            rel, target = rel_target.split(' -> ')
            G.add_node(source, node_type='Entity')
            G.add_node(target, node_type='Entity')
            G.add_edge(source, target, relationship=rel)
    return G

def visualize_graph(G: nx.Graph):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=8, font_weight='bold')
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'relationship')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    return plt

def main():
    st.title("Disease Information App")

    user_question = st.text_input("Ask a question about diseases, symptoms, causes, risk factors, or treatments:")

    if user_question:
        # Use structured retriever to get results
        result = structured_retriever(user_question)
        st.write(result)
        st.subheader("Retrieved Information:")
        st.text(result)

        # Create and visualize graph
        if result:
            G = create_graph_from_result(result)
            fig = visualize_graph(G)
            st.pyplot(fig)
        else:
            st.write("No results found for your query.")

if __name__ == "__main__":
    main()
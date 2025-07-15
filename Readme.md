# Knowledge Graph for Medical Information

A comprehensive knowledge graph implementation for medical data using Neo4j, LangChain, and Google's Gemini LLM to transform healthcare datasets into an interactive graph database.

## 🔍 Overview

This project creates a knowledge graph from medical datasets, specifically focusing on diseases, symptoms, causes, risk factors, and treatments. The system uses Large Language Models (LLM) to extract entities and relationships from structured data and stores them in a Neo4j graph database for efficient querying and visualization.

## 🏗️ Architecture

The project consists of several key components:

- **Data Processing**: Converts CSV medical data into graph documents using LangChain
- **Graph Database**: Neo4j AuraDB for storing nodes and relationships
- **LLM Integration**: Google Gemini 1.5 Flash for entity extraction and relationship mapping
- **Visualization**: Interactive graph visualization using yFiles and NetworkX
- **Web Interface**: Streamlit application for querying the knowledge graph

## 📁 Project Structure

```
├── app.py                    # Streamlit web application
├── Graph_RAG.ipynb         # Main notebook for graph creation and RAG implementation
├── experiment.ipynb        # Experimental notebook with predefined nodes/relationships
├── demo_experiment.ipynb   # Demo experiments and testing
├── data_format.ipynb       # Data formatting and preprocessing
└── Readme.md              # Project documentation
```

## 🚀 Features

- **Knowledge Graph Construction**: Automated transformation of medical data into graph format
- **Entity Extraction**: AI-powered extraction of diseases, symptoms, causes, and treatments
- **Graph Visualization**: Interactive graph visualization with node relationships
- **Query Interface**: Natural language querying through Streamlit web interface
- **RAG Implementation**: Retrieval-Augmented Generation for intelligent responses
- **Batch Processing**: Efficient processing of large datasets in manageable chunks

## 🛠️ Technology Stack

- **Database**: Neo4j AuraDB
- **LLM**: Google Gemini 1.5 Flash
- **Framework**: LangChain
- **Visualization**: NetworkX, yFiles, Matplotlib
- **Web Interface**: Streamlit
- **Data Processing**: Pandas, Pickle
- **Environment**: Python 3.x

## 📋 Prerequisites

Before running this project, ensure you have:

1. **Neo4j AuraDB Account**: Create a free account at [Neo4j Aura](https://neo4j.com/cloud/aura/)
2. **Google AI API Key**: Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Python 3.8+**: Ensure Python is installed on your system

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Knowledge_Graph
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit neo4j networkx matplotlib py2neo
   pip install langchain-community langchain-experimental
   pip install google-generativeai python-dotenv
   pip install yfiles-jupyter-graphs pandas pickle5
   ```

3. **Environment Setup**:
   Create a `.env` file in the project root:
   ```env
   NEO4J_URI=your_neo4j_uri
   NEO4J_USERNAME=your_username
   NEO4J_PASSWORD=your_password
   GOOGLE_API_KEY=your_google_api_key
   ```

## 🎯 Usage

### Running the Web Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The web interface allows you to:
- Ask questions about diseases, symptoms, and treatments
- Visualize relationship graphs
- Explore entity connections

### Working with Notebooks

1. **Graph_RAG.ipynb**: Main implementation for creating and querying the knowledge graph
2. **experiment.ipynb**: Experiments with predefined node types and relationships
3. **demo_experiment.ipynb**: Demo implementations and testing scenarios
4. **data_format.ipynb**: Data preprocessing and formatting utilities

### Key Functions

- **Entity Extraction**: `extract_entities(question)` - Extracts medical entities from text
- **Structured Retrieval**: `structured_retriever(question)` - Retrieves related information from graph
- **Graph Visualization**: `visualize_graph(G)` - Creates interactive graph visualizations

## 📊 Data Format

The system expects medical data in CSV format with fields like:
- Disease names
- Symptoms
- Causes
- Risk factors
- Treatments
- Medical links and references

## 🔗 Graph Schema

The knowledge graph contains:

**Node Types**:
- Diseases
- Symptoms
- Causes
- Risk Factors
- Treatments

**Relationship Types**:
- HAS_SYMPTOM
- CAUSED_BY
- TREATED_WITH
- RISK_FACTOR_FOR
- BASED_ON

## 📈 Performance

- Processes datasets with 1000+ medical records
- Batch processing in chunks of 10 documents
- Supports error handling and retry mechanisms
- Optimized for large-scale medical datasets

## 🙏 Acknowledgments

- Neo4j for the graph database platform
- Google for the Gemini LLM API
- LangChain community for the transformation tools
- Medical data sources and healthcare communities



---

**Note**: This project is for educational and research purposes. Always consult healthcare professionals for medical advice.
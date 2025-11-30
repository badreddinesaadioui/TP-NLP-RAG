## Group members

- **Oussama Hajji**
- **Membre2**
- **Membre2**
- **Membre2**

# RAG Chatbot – Retrieval-Augmented Generation

This project implements an intelligent chatbot using a RAG (Retrieval-Augmented Generation) architecture to answer user questions based on a collection of PDF documents.
The system combines document extraction, vector search, and text generation using an LLM, utilizing research papers on LLMs as reference documents. It helps researchers perform benchmarks on the topic and understand how each article attempts to solve a problem without wasting too much time.

## 1. Features
- Automatic PDF loading
- Splitting documents into chunks
- Embedding generation
- Vector storage (cosine similarity)
- Retrieval of the most relevant passages
- Command-line interface (cli.py)
- Web interface via Streamlit


---

## 2. Project Architecture

RAG/
│
├── app.py                  # Interface Streamlit  
├── cli.py                  # Chatbot en terminal  
│
├── data/  
│   └── documentation/               # Dossier des PDF  
│
├── src/  
│   ├── loader.py  # Chargement des PDF  
│   ├── vector_store.py     # Index vectoriel (ChromaDB / cosine)  
│   └── chatbot.py          # Gestion du chat + historique  
│
│
└──requirments.txt
└── README.md



---

## 3. Installation


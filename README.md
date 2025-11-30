## Group members

- **Oussama Hajji**
- **Membre2**
- **Membre2**
- **Membre2**

# RAG Chatbot – Retrieval-Augmented Generation

This project implements an intelligent chatbot using a RAG (Retrieval-Augmented Generation) architecture to answer user questions based on a collection of PDF documents.
The system combines document extraction, vector search, and text generation using an LLM, utilizing research papers on LLMs as reference documents. It helps researchers perform benchmarks on the topic and understand how each article attempts to solve a problem without wasting too much time.

## 1. Fonctionnalités

- Chargement automatique des PDF
- Découpage des documents en chunks
- Génération d’embeddings
- Stockage vectoriel (similarité cosinus)
- Récupération des passages les plus pertinents
- Génération des réponses via Google Gemini
- Interface en ligne de commande (CLI)
- Interface web via Streamlit

---

## 2. Architecture du projet

RAG/
│
├── app.py                  # Interface Streamlit  
├── cli.py                  # Chatbot en terminal  
│
├── data/  
│   └── pdfs/               # Dossier des PDF  
│
├── src/  
│   ├── document_loader.py  # Chargement des PDF  
│   ├── text_splitter.py    # Découpage en chunks  
│   ├── embedding_model.py  # Génération d'embeddings  
│   ├── vector_store.py     # Index vectoriel (FAISS / cosine)  
│   ├── retriever.py        # Recherche des chunks pertinents  
│   ├── llm_model.py        # Appel au modèle Gemini  
│   ├── rag_pipeline.py     # Pipeline RAG (context + prompt)  
│   └── chatbot.py          # Gestion du chat + historique  
│
└── README.md



---

## 3. Installation


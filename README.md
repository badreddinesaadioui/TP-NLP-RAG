# TP-NLP-RAG
📚 RAG Chatbot — Retrieval-Augmented Generation

Ce projet implémente un chatbot intelligent capable de répondre à des questions en utilisant le contenu de vos documents PDF grâce à une architecture RAG (Retrieval-Augmented Generation).

Le chatbot utilise :

extraction de texte PDF

découpage en chunks

embeddings vectoriels

recherche par similarité

génération de réponses via Google Gemini

interface web Streamlit

🚀 Fonctionnalités

📄 Lecture automatique des PDF depuis data/pdfs/

✂️ Découpage du texte en chunks optimisés

🧠 Génération d'embeddings (sentence-transformers)

📦 Stockage vectoriel custom (cosine similarity)

🔍 Récupération des documents pertinents

🤖 Réponse générée avec Gemini

🌐 Interface web via Streamlit

🖥️ Interface CLI pour usage terminal

🏗️ Architecture du projet
RAG/
│
├── app.py                     # Interface Streamlit
├── cli.py                     # Chatbot en mode terminal
│
├── data/
│   └── pdfs/                  # Vos documents PDF
│
├── src/
│   ├── document_loader.py     # Extraction PDF
│   ├── text_splitter.py       # Split en chunks
│   ├── embedding_model.py     # Embeddings
│   ├── vector_store.py        # Index vectoriel
│   ├── retriever.py           # Recherche
│   ├── llm_model.py           # LLM Gemini
│   ├── rag_pipeline.py        # Pipeline RAG
│   └── chatbot.py             # Chatbot final
│
└── README.md

⚙️ Installation
1. Cloner le projet
git clone <URL_DU_REPO>
cd RAG

2. Installer les dépendances
pip install -r requirements.txt

3. Ajouter la clé API Gemini
Windows (PowerShell)
setx GEMINI_API_KEY "VOTRE_CLE_ICI"

Linux / macOS
export GEMINI_API_KEY="VOTRE_CLE_ICI"


Ensuite, redémarre VS Code ou le terminal pour appliquer les variables d'environnement.

▶️ Utilisation
🔹 1. Mode CLI (terminal)
python cli.py

🔹 2. Mode Web avec Streamlit
streamlit run app.py


👀 L'application s’ouvrira sur :
👉 http://localhost:8501

🧠 Comment fonctionne le RAG ?

Tu poses une question

Le système convertit ta question en embedding

Il cherche les chunks PDF les plus proches

Le contexte trouvé est ajouté à la question

Le tout est envoyé au LLM Gemini

Le LLM génère une réponse basée sur :

ta question

les passages pertinents du PDF

📌 Exemple d'utilisation

→ Déposez des fichiers PDF dans data/pdfs/
→ Lancez l’appli Streamlit
→ Entrez une question, par exemple :

"Quels sont les points clés du document 1 ?"

Le chatbot analysera vos PDF et générera une réponse enrichie.

🧰 Technologies utilisées

Python 3

PyPDF2

sentence-transformers

NumPy

Google Gemini API

Streamlit

Vector Search (cosine similarity)

👥 Membres du groupe

Hajji Oussama

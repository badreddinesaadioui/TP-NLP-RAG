# TP-NLP-RAG
\documentclass[12pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{graphicx}

\geometry{margin=2cm}

% Style des sections
\titleformat{\section}{\large\bfseries}{\thesection.}{1em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection.}{1em}{}

% Code style
\lstset{
    basicstyle=\ttfamily\small,
    backgroundcolor=\color{gray!10},
    frame=single,
    breaklines=true
}

\begin{document}

% -------------------------------------------------------------------
\begin{center}
    {\LARGE \textbf{Projet RAG -- Retrieval-Augmented Generation}}\\[0.5cm]
    {\large Rapport technique / README en \LaTeX}\\[0.5cm]
\end{center}
% -------------------------------------------------------------------

\section*{Objectif du Projet}

L'objectif de ce projet est de concevoir un système complet appelés RAG (\textit{Retrieval-Augmented Generation}).  
Il s'agit d'un chatbot intelligent capable d'utiliser des documents PDF fournis par l'utilisateur pour générer des réponses contextualisées grâce à un modèle de langage (LLM).

Ce système repose sur :
\begin{itemize}
    \item l'extraction et le traitement de documents PDF,
    \item la génération d'embeddings vectoriels,
    \item la recherche par similarité,
    \item la génération de texte via le modèle Google Gemini,
    \item une interface utilisateur avec Streamlit.
\end{itemize}

% -------------------------------------------------------------------
\section{Architecture Globale}

\begin{lstlisting}
RAG/
│
├── app.py                      # Interface Streamlit
├── cli.py                      # Interface CLI
│
├── data/
│   └── pdfs/                   # Documents PDF
│
├── src/
│   ├── document_loader.py      # Chargement PDF
│   ├── text_splitter.py        # Découpage en chunks
│   ├── embedding_model.py      # Embeddings
│   ├── vector_store.py         # Index vectoriel
│   ├── retriever.py            # Recherche de similarité
│   ├── llm_model.py            # Appel Gemini
│   ├── rag_pipeline.py         # Pipeline RAG
│   └── chatbot.py              # Chatbot
│
└── README.tex
\end{lstlisting}

% -------------------------------------------------------------------
\section{Fonctionnement du Système}

\subsection{1. Chargement des Documents}
Les fichiers PDF présents dans \texttt{data/pdfs} sont automatiquement chargés et analysés.

\subsection{2. Découpage en Chunks}
Le texte est découpé en segments plus courts afin d'améliorer la recherche et la qualité des embeddings.

\subsection{3. Génération des Embeddings}
Chaque chunk est encodé en vecteur numérique via un modèle de type \texttt{SentenceTransformer}.

\subsection{4. Index Vectoriel}
Les vecteurs sont stockés dans une base interne permettant des recherches rapides par similarité.

\subsection{5. Recherche de Contexte}
Lorsqu'une question est posée, les chunks les plus pertinents sont sélectionnés grâce à la similarité cosinus.

\subsection{6. Génération de Réponse (LLM)}
Le modèle Google Gemini reçoit :
\begin{itemize}
    \item la question,
    \item les documents pertinents retrouvés.
\end{itemize}
Il génère ensuite une réponse enrichie.

\subsection{7. Interface Utilisateur}
Le chatbot est disponible via :
\begin{itemize}
    \item une interface CLI (\texttt{cli.py}),
    \item une application web Streamlit (\texttt{app.py}).
\end{itemize}

% -------------------------------------------------------------------
\section{Installation}

\subsection{1. Cloner le projet}
\begin{lstlisting}
git clone <URL-du-repo>
cd RAG
\end{lstlisting}

\subsection{2. Installer les dépendances}
\begin{lstlisting}
pip install -r requirements.txt
\end{lstlisting}

\subsection{3. Configurer l’API Key Gemini}

\textbf{Windows (PowerShell) :}
\begin{lstlisting}
setx GEMINI_API_KEY "VOTRE_CLE_ICI"
\end{lstlisting}

\textbf{Linux / macOS :}
\begin{lstlisting}
export GEMINI_API_KEY="VOTRE_CLE_ICI"
\end{lstlisting}

Redémarrer le terminal ou VS Code pour appliquer la configuration.

% -------------------------------------------------------------------
\section{Utilisation}

\subsection{Interface CLI}
\begin{lstlisting}
python cli.py
\end{lstlisting}

\subsection{Interface Streamlit}
\begin{lstlisting}
python -m streamlit run app.py
\end{lstlisting}

L'application sera disponible à l'adresse :

\begin{center}
\textbf{http://localhost:8501}
\end{center}

% -------------------------------------------------------------------
\section{Exemple d’Interaction}

\begin{enumerate}
    \item Déposer des fichiers PDF dans \texttt{data/pdfs}
    \item Lancer l'application
    \item Poser une question, par exemple :

    \textit{"Quels sont les points importants du premier document ?"}

    \item Le système extrait les passages pertinents et fournit une réponse générée par Gemini.
\end{enumerate}

% -------------------------------------------------------------------
\section{Technologies Utilisées}

\begin{itemize}
    \item \textbf{Python}
    \item \textbf{PyPDF2} -- Extraction PDF
    \item \textbf{SentenceTransformer} -- Embeddings
    \item \textbf{Numpy} -- Similarité cosinus
    \item \textbf{Google Gemini} -- Modèle LLM
    \item \textbf{Streamlit} -- Interface web
\end{itemize}

% -------------------------------------------------------------------
\section{Membres du Groupe}

\begin{itemize}
    \item Oussama Hajji
    \item (Ajouter les autres membres)
\end{itemize}

% -------------------------------------------------------------------
\section*{Licence}

Projet réalisé dans le cadre universitaire. Utilisation libre à des fins éducatives.

\end{document}

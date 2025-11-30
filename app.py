import streamlit as st
from src.loader import DocumentLoader
from src.vector_store import VectorStore
from src.chatbot import RAGChatbot
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()

st.set_page_config(page_title="RAG NLP Project")

@st.cache_resource(show_spinner=False)
def initialize_system():
    # Load API Key from secrets if not in env
    if "OPENAI_API_KEY" not in os.environ and "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

    loader = DocumentLoader("data")
    loader.load_documents()
    chunks = loader.get_chunked_text()
    
    vector_store = VectorStore()
    # Check if index exists, if not create it (or just always recreate for demo)
    vector_store.create_vector_store(chunks)
    
    bot = RAGChatbot()
    return vector_store, bot

def main():
    st.title("🤖 NLP RAG Chatbot")
    
    status_text = st.empty()
    status_text.text("Initializing system...")
    
    try:
        vector_store, bot = initialize_system()
        status_text.empty()
    except Exception as e:
        st.error(f"Error initializing: {e}")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Search and Generate
        results = vector_store.search(prompt)
        context_docs = [doc for doc, score in results]
        
        # LangChain Chain
        chain = bot.get_rag_chain(vector_store.vectorstore)
        response = chain.invoke(prompt)
        
        # Evaluation
        score = bot.evaluate_answer(prompt, response, context_docs)

        full_response = f"{response}\n\n---\n*Relevance Score: {score}/10*"
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        with st.chat_message("assistant"):
            st.markdown(full_response)

if __name__ == "__main__":
    main()

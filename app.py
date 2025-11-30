import streamlit as st
import os

st.set_page_config(page_title="RAG NLP Project", layout="wide")

def main():
    st.title("🤖 NLP RAG Chatbot")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about the documents..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            st.markdown("Backend not connected yet. Waiting for team implementation...")

if __name__ == "__main__":
    main()


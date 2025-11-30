import os
import argparse
from dotenv import load_dotenv
from src.loader import DocumentLoader
from src.vector_store import VectorStore
from src.chatbot import RAGChatbot

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="RAG CLI Tool")
    parser.add_argument("--query", type=str, help="The question to ask")
    parser.add_argument("--index", action="store_true", help="Re-index the documents")
    
    args = parser.parse_args()
    
    # Initialize components
    loader = DocumentLoader("data")
    vector_store = VectorStore()
    bot = RAGChatbot()
    
    if args.index:
        print("Loading documents...")
        loader.load_documents()
        chunks = loader.get_chunked_text()
        print(f"Created {len(chunks)} chunks.")
        
        print("Creating vector store (Embeddings)...")
        vector_store.create_vector_store(chunks)
        print("Indexing complete.")
        
    if args.query:
        print(f"\nQuery: {args.query}")
        
        # Search
        results = vector_store.search(args.query)
        context_docs = [doc for doc, score in results]
        
        # Generate Answer
        # We need to load the vectorstore first to get the retriever
        vector_store.load_vector_store()
        chain = bot.get_rag_chain(vector_store.vectorstore)
        
        print("\nGenerating answer...")
        response = chain.invoke(args.query)
        
        print(f"\nAnswer: {response}")
        
        # Evaluation (Q4)
        print("\nEvaluating answer...")
        score = bot.evaluate_answer(args.query, response, context_docs)
        print(f"Relevance Score: {score}/10")

        print("\nSources:")
        for doc, score in results:
            print(f"- {doc.metadata.get('source', 'Unknown')} (Score: {score:.4f})")

if __name__ == "__main__":
    main()

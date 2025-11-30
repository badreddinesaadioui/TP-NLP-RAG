from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
import shutil

class VectorStore:
    def __init__(self, collection_name="rag_collection", persist_directory="./chroma_db"):
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = None

    def create_vector_store(self, chunks):
        if os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
            
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
            collection_name=self.collection_name
        )

    def load_vector_store(self):
        self.vectorstore = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
            collection_name=self.collection_name
        )

    def search(self, query, k=3):
        if not self.vectorstore:
            self.load_vector_store()
        results = self.vectorstore.similarity_search_with_score(query, k=k)
        return results

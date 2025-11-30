from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

class DocumentLoader:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.documents = []

    def load_documents(self):
        # Check if directory exists
        if not os.path.exists(self.directory_path):
            os.makedirs(self.directory_path, exist_ok=True)
            return []
            
        pdf_files = [f for f in os.listdir(self.directory_path) if f.endswith('.pdf')]
        all_docs = []
        
        for filename in pdf_files:
            file_path = os.path.join(self.directory_path, filename)
            loader = PyPDFLoader(file_path)
            all_docs.extend(loader.load())
            
        self.documents = all_docs
        return self.documents

    def get_chunked_text(self, chunk_size=1000, chunk_overlap=200):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            add_start_index=True
        )
        if not self.documents:
            return []
        return text_splitter.split_documents(self.documents)

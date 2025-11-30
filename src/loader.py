import os
from pypdf import PdfReader


class DocumentLoader:
    """Loads PDF documents from a directory and extracts their text."""

    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        self.documents = []

    def load_documents(self):
        """
        Load all PDF documents from the directory and extract their text.
        Includes Streamlit progress UI components.
        """
        import streamlit as st

        pdf_files = [
            f for f in os.listdir(self.directory_path)
            if f.lower().endswith('.pdf')
        ]

        status_text = st.empty()
        status_text.write("Starting PDF processing...")
        progress_bar = st.progress(0)

        total_files = len(pdf_files)
        for idx, filename in enumerate(pdf_files):
            file_path = os.path.join(self.directory_path, filename)

            status_text.write(f"Reading {filename}...")
            self._read_pdf(file_path)

            progress_bar.progress((idx + 1) / total_files)

        status_text.empty()
        progress_bar.empty()

        return self.documents

    def _read_pdf(self, file_path: str):
        """Extract text from a PDF file and store it in the documents list."""
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        self.documents.append({
            "source": file_path,
            "text": text.strip()
        })

    def get_chunked_text(self, chunk_size: int = 1000):
        """
        Split all loaded documents into chunks of a given size.

        :param chunk_size: Maximum size of each text chunk.
        :return: List of text chunks.
        """
        chunks = []

        for doc in self.documents:
            text = doc["text"]
            for i in range(0, len(text), chunk_size):
                chunks.append(text[i:i + chunk_size])

        return chunks

import os
from typing import List, Dict, Generator, Optional
from pypdf import PdfReader


class DocumentLoader:
    """Loads PDF documents from a directory and extracts their text efficiently."""

    def __init__(self, directory_path: str):
        if not os.path.isdir(directory_path):
            raise ValueError(f"Invalid directory: {directory_path}")

        self.directory_path = directory_path
        self.documents: List[Dict[str, str]] = []

    def load_documents(self, use_streamlit: bool = False):
        """
        Load all PDF documents and extract text.
        If use_streamlit=True, displays a progress bar.
        """
        pdf_files = [
            f for f in os.listdir(self.directory_path)
            if f.lower().endswith(".pdf")
        ]

        status_text = progress_bar = None
        if use_streamlit:
            import streamlit as st
            status_text = st.empty()
            progress_bar = st.progress(0)
            status_text.write("Starting PDF processing...")

        total = len(pdf_files)
        for i, filename in enumerate(pdf_files):
            file_path = os.path.join(self.directory_path, filename)

            if status_text:
                status_text.write(f"Reading {filename}...")

            self.documents.append({
                "source": file_path,
                "text": self._extract_pdf_text(file_path)
            })

            if progress_bar:
                progress_bar.progress((i + 1) / total)

        if status_text:
            status_text.empty()
        if progress_bar:
            progress_bar.empty()

        return self.documents

    @staticmethod
    def _extract_pdf_text(file_path: str) -> str:
        """Extract all text from a PDF file (optimized)."""
        reader = PdfReader(file_path)

        # Générateur optimisé (évite concaténation répétée)
        lines: Generator[str, None, None] = (
            page.extract_text() or ""
            for page in reader.pages
        )

        return "\n".join(lines).strip()

    def get_chunked_text(self, chunk_size: int = 1000) -> List[str]:
        """Split all documents into text chunks of a given size."""
        if chunk_size <= 0:
            raise ValueError("chunk_size must be > 0")

        chunks: List[str] = []

        for doc in self.documents:
            text = doc["text"]
            chunks.extend(
                text[i:i + chunk_size]
                for i in range(0, len(text), chunk_size)
            )

        return chunks

import chromadb
from chromadb.config import Settings

class VectorStore:
    def __init__(self, dimension):
        self.client = chromadb.Client(Settings(anonymized_telemetry=False))

        # La collection persiste automatiquement en local
        self.collection = self.client.get_or_create_collection(
            name="rag_collection",
            metadata={"hnsw:space": "cosine"}  # mesure de similarité
        )

    def add_embeddings(self, embeddings, texts):
        ids = [f"id_{i}" for i in range(len(texts))]
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts
        )

    def search(self, query_embedding, k=3):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
        return results["documents"][0]

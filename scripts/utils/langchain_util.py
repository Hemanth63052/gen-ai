import faiss
import numpy as np
from typing import List

class FAISSUtil:
    def __init__(self, embedding_dim=768):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []

    def store_embedding(self, chunk_id: str, chunk_text: str, embedding: List[float]):
        vector = np.array(embedding).astype("float32").reshape(1, -1)
        self.index.add(vector)
        self.metadata.append({"id": chunk_id, "text": chunk_text})

    def search_similar_chunks(self, query_embedding: List[float], k: int = 5):
        query_vector = np.array(query_embedding).astype("float32").reshape(1, -1)
        distances, indices = self.index.search(query_vector, k)

        results = [{"id": self.metadata[i]["id"], "text": self.metadata[i]["text"], "distance": distances[0][j]}
                   for j, i in enumerate(indices[0])]
        return results

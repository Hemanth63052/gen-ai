import chromadb


class ChromaDBUtil:
    def __init__(self):
        self.chrom_db_dir = None
        client = chromadb.Client()
        self.collection = client.get_or_create_collection(name="0123456789abcdef0123456789abcdef_pdf_embeddings")

    def store_embedding(self, embedding_id, text_chunk, embedding_vector):
        self.collection.add(
            documents=[text_chunk],
            embeddings=[embedding_vector],
            ids=[embedding_id]
        )

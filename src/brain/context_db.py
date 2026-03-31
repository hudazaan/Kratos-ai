import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

class KratosContext:
    def __init__(self):
        db_path = os.getenv("DB_PATH", "./data/chroma_db")
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(name="project_context")

    def add_code(self, file_path, content):
        self.collection.add(
            documents=[content],
            metadatas=[{"path": file_path}],
            ids=[file_path]
        )

    def get_relevant_context(self, diff):
        results = self.collection.query(query_texts=[diff], n_results=2)
        return "\n".join(results['documents'][0]) if results['documents'] else ""
import chromadb
import os
from pathlib import Path # Add this import at the top
from dotenv import load_dotenv

load_dotenv()

class KratosContext:
    def __init__(self):
        # 1. Get the path from your variable: DB_PATH
        db_path = os.getenv("DB_PATH", "./data/chroma_db")
        
        # 2. THE FIX: Ensure the directory exists before ChromaDB starts
        # This creates the 'data' folder automatically in the cloud
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        
        # 3. Now initialize the client
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(name="project_context")
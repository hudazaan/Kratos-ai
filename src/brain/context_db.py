import chromadb
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class KratosContext:
    def __init__(self):
        
        base_dir = os.getcwd()

        db_dir = os.path.join(base_dir, "kratos_memory")

        if not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
            
        print(f"DEBUG: Attempting to open DB at: {db_dir}")

        self.client = chromadb.PersistentClient(path=db_dir)
        self.collection = self.client.get_or_create_collection(name="project_context")
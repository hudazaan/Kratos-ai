import os
from brain.context_db import KratosContext

def index_all():
    db = KratosContext(path=os.getenv("DB_PATH", "kratos_memory"))
    
    # List of files you want the AI to "know" about
    files_to_index = [
        "src/pipeline/scrubber.py",
        "src/pipeline/gh_client.py",
        "src/main.py"
    ]
    
    for file_path in files_to_index:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()
                # Assuming your KratosContext has an add_context method
                db.add_context(file_path, content)
                print(f"✅ Indexed {file_path}")

if __name__ == "__main__":
    index_all()
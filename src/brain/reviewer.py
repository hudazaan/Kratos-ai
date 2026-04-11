import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

class KratosBrain:
    def __init__(self):
        token = os.getenv("HF_TOKEN")
        if not token:
            raise ValueError("HF_TOKEN not found in .env")
        
        self.client = InferenceClient(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            token=token.strip()
        )

    def analyze(self, diff, context):
        try:
            # We use chat_completion to satisfy the 'conversational' task requirement
            response = self.client.chat_completion(
                messages=[
                    {"role": "system", "content": "You are a Senior Engineer. Review this code for bugs and security risks. If it's fine, reply only 'LGTM'."},
                    {"role": "user", "content": f"Context: {context}\n\nDiff: {diff}"}
                ],
                max_tokens=500,
                temperature=0.1
            )
            return response.choices[0].message.content
            
        except Exception as e:
            return f"AI Error: {str(e)}"
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

class KratosBrain:
    def __init__(self):

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file")
            
        self.client = genai.Client(api_key=api_key)
        self.model_id = 'gemini-1.5-flash' 

    def analyze(self, diff, context):
        prompt = f"""
        Act as a Senior Engineer. Review this diff with the provided project context.
        
        CONTEXT: {context}
        
        DIFF: {diff}
        
        INSTRUCTIONS:
        - Identify critical bugs or security risks.
        - If the code is fine, reply only with 'LGTM'.
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error during AI analysis: {str(e)}"
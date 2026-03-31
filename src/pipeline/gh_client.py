import requests
import os

class GitHubClient:
    def __init__(self):
        self.token = os.getenv("GITH_TOKEN")
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def post_comment(self, repo, pr_number, body):
        url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
        payload = {"body": f"### Kratos AI Review\n\n{body}"}
        
        response = requests.post(url, json=payload, headers=self.headers)
        
        if response.status_code != 201:
            print(f" Error: Received {response.status_code} from GitHub.")
            print(f" Message: {response.json().get('message')}")
        
        return response.status_code
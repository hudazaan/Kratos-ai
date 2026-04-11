import os
import sys
from brain.context_db import KratosContext
from brain.reviewer import KratosBrain
from pipeline.diff_parser import clean_diff
from pipeline.gh_client import GitHubClient
from pipeline.scrubber import mask_secrets

def run_kratos(repo, pr_number, raw_diff):
    print("Initializing Kratos AI..")
    db = KratosContext()
    brain = KratosBrain()
    gh = GitHubClient()

    # Get Context + Generate Review
    diff = clean_diff(raw_diff)
    context = db.get_relevant_context(diff)
    review = brain.analyze(diff, context)
    print(f"DEBUG: AI Review Output: '{review}'")

    # Scrub secrets before posting 
    clean_review = mask_secrets(review) or ""

    print(f"--- DEBUG: SCRUBBED REVIEW ---\n{clean_review}\n--------------")
   
    # if "LGTM" not in clean_review and len(clean_review.strip()) > 10: 
    #     status = gh.post_comment(repo, pr_number, clean_review)
    #     print(f"✅ Review posted with status: {status}")
    # else:
    #     print("🚀 Code looks good or review was too short. No comments posted.")
    if len(clean_review.strip()) > 10: 
        status = gh.post_comment(repo, pr_number, clean_review)
        print(f"✅ Review posted with status: {status}")
    else:
        print("🚀 Review was too short. No comments posted.")
        
    # # DevOps Logic: Post to GitHub
    # print(f"DEBUG: AI Review Output: '{review}'") # Add this line!

    # if "LGTM" not in review and len(review.strip()) > 5:
    #     status = gh.post_comment(repo, pr_number, review)
    #     print(f"✅ Review posted with status: {status}")
    # else:
    #     print("🚀 Code looks good or review was too short. No comments posted.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❌ Usage: python main.py <repo_name> <pr_number>")
        sys.exit(1)

    repo_name = sys.argv[1]
    pr_num = sys.argv[2]

    # Ensure diff.txt exists for the local test
    if not os.path.exists("diff.txt"):
        with open("diff.txt", "w") as f:
            f.write("+ def test():\n+     pass")

    with open("diff.txt", "r") as f:
        diff_content = f.read()
    
    run_kratos(repo_name, pr_num, diff_content)
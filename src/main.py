import os
import sys
from brain.context_db import KratosContext
from brain.reviewer import KratosBrain
from pipeline.diff_parser import clean_diff
from pipeline.gh_client import GitHubClient

def run_kratos(repo, pr_number, raw_diff):
    # Init
    db = KratosContext()
    brain = KratosBrain()
    gh = GitHubClient()

    # ML Logic: Get Context + Generate Review
    diff = clean_diff(raw_diff)
    context = db.get_relevant_context(diff)
    review = brain.analyze(diff, context)

    # DevOps Logic: Post to GitHub
    print(f"DEBUG: AI Review Output: '{review}'") # Add this line!

    if "LGTM" not in review and len(review.strip()) > 5:
        status = gh.post_comment(repo, pr_number, review)
        print(f"✅ Review posted with status: {status}")
    else:
        print("🚀 Code looks good or review was too short. No comments posted.")

if __name__ == "__main__":
    repo_name = sys.argv[1]
    pr_num = sys.argv[2]
    with open("diff.txt", "r") as f:
        diff_content = f.read()
    
    run_kratos(repo_name, pr_num, diff_content)
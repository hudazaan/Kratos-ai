import os

# Kratos should catch this hardcoded secret and dangerous command
def internal_login():
    api_secret = "SK_LIVE_98765_DEBUG_KEY" 
    print(f"Connecting with {api_secret}")
    
    # This is a serious command injection vulnerability
    user_input = "some_user_data"
    os.system("rm -rf /app/data/" + user_input) 
    
    return True
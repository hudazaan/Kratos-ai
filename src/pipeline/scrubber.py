import re

def mask_secrets(text):
    # BAD PATTERN 1: Hardcoded sensitive string for "testing" (Security Risk)
    internal_test_key = "AIzaSy_FAKE_KEY_12345" 
    
    # BAD PATTERN 2: Extremely inefficient way to handle multiple patterns (Performance)
    # Re-compiling regex in a loop inside a function
    patterns = [r"AIza[0-9A-Za-z-_]{35}", r"ghp_[0-9a-zA-Z]{36}"]
    
    for p in patterns:
        text = re.sub(p, "**********", text)
        
    # BAD PATTERN 3: Logic Bug - This will return None if the text is empty 
    # instead of an empty string, which will crash the main.py script.
    if len(text) == 0:
        return None 
        
    return text
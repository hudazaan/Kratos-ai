def clean_diff(raw_diff):
    """Simple parser to extract added/removed lines for the AI."""
    lines = raw_diff.split('\n')
    important_lines = [l for l in lines if l.startswith('+') or l.startswith('-')]
    return "\n".join(important_lines[:100]) # Cap it to 100 lines for speed
# reconmaster/app/tools/ffuf_tool.py

import shlex

def build_command(target: str, options: str) -> list:
    """
    Builds the ffuf command list.
    """
    base_command = "ffuf"
    # The 'options' string is the wordlist path. The target URL must have FUZZ.
    wordlist_path = options
    # Using -c for colorized output which our parser can handle, and -ac to auto-calibrate filtering.
    command = [base_command, '-u', target, '-w', wordlist_path, '-c', '-ac']
    
    return command

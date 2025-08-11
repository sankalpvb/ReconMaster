# reconmaster/app/tools/gobuster_tool.py

def build_command(target: str, options: str) -> list:
    """
    Builds the Gobuster command list from the target and options.
    """
    base_command = "gobuster"
    
    # The 'options' string we receive from the UI is the wordlist path.
    wordlist_path = options
    
    # We construct the command with the 'dir' subcommand and use '-z' to show size.
    command = [base_command, 'dir', '-u', target, '-w', wordlist_path, '-t', '30', '-z']
    
    return command

# reconmaster/app/tools/whois_tool.py

def build_command(target: str, options: str) -> list:
    """
    Builds the whois command list from the target domain.
    'options' are not used for this tool.
    """
    base_command = "whois"
    
    # The command is simply 'whois' followed by the target domain.
    command = [base_command, target]
    
    return command

# reconmaster/app/tools/assetfinder_tool.py

def build_command(target: str, options: str) -> list:
    """
    Builds the assetfinder command list from the target domain.
    """
    base_command = "assetfinder"
    
    # --subs-only ensures we only get subdomains back
    command = [base_command, '--subs-only', target]
    
    return command

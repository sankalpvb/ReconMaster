# reconmaster/app/tools/httpx_tool.py

def build_command(target: str, options: str) -> list:
    """
    Builds the httpx command list.
    Note: httpx is designed to take a list of hosts from stdin,
    but for a single target, we can pass it directly.
    """
    base_command = "httpx"
    
    # We will run httpx with flags to get useful information:
    # -sc: Show status code (Corrected from -s)
    # -title: Show page title
    # -tech-detect: Show technologies detected
    # -no-color: Ensures clean output for our parser
    command = [
        base_command,
        '-sc',
        '-title',
        '-tech-detect',
        '-silent',
        '-no-color',
        '-u', # Specify the URL
        target
    ]
    
    return command

# reconmaster/app/tools/whatweb_tool.py

def build_command(target: str, options: str) -> list:
    """
    Builds the WhatWeb command list from the target URL.
    The 'options' are not used for this simple tool but are kept for consistency.
    """
    base_command = "whatweb"
    
    # We add an aggression level of 1 (-a 1) for a balance of speed and detail.
    # WhatWeb's primary argument is just the target URL.
    command = [base_command, '-a', '1', target]
    
    return command

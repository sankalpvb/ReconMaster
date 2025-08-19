# reconmaster/app/tools/sublist3r_tool.py

def build_command(target: str, options: str) -> list:
    """
    Builds the Sublist3r command list from the target domain.
    The 'options' are not used for this simple tool but are kept for consistency.
    """
    base_command = "sublist3r"
    
    # Sublist3r's primary argument is -d for domain.
    command = [base_command, '-d', target]
    
    return command

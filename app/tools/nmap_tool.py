# reconmaster/app/tools/nmap_tool.py
import shlex

def build_command(target: str, options: str) -> list:
    """
    Builds the Nmap command list from the target and options.
    """
    base_command = "nmap"
    
    # Safely split the options string into a list of arguments.
    # For example, "-T4 -sV" becomes ['-T4', '-sV']
    options_list = shlex.split(options)
    
    # The final command is the base, followed by options, and then the target.
    command = [base_command] + options_list + [target]
    
    return command

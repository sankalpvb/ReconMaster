# reconmaster/app/services/sublist3r_suggester.py

def get_suggestion(subdomain: str) -> str:
    """
    Takes a discovered subdomain and returns a relevant suggestion.
    """
    # The suggestion is always the same for any found subdomain.
    return "Subdomain found. Consider running an Nmap scan on this host to discover open ports and services."

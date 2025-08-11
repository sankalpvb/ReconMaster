# reconmaster/app/services/suggestion_engine.py

# A dictionary where keys are keywords and values are suggested actions.
# We check if a keyword is present in the service string.
SUGGESTION_MAP = {
    "http": "Web server found. Consider running Gobuster for directory brute-forcing or Nikto for vulnerability scanning.",
    "https": "Secure web server found. Check for SSL/TLS misconfigurations and run web application scans.",
    "ssh": "SSH service found. Consider checking for weak credentials or using a tool like Hydra for brute-force attacks (with permission).",
    "ftp": "FTP service found. Check for anonymous login vulnerabilities.",
    "smb": "SMB (Windows file sharing) found. Check for vulnerabilities like EternalBlue or use Enum4linux to enumerate shares.",
    "smtp": "SMTP mail server found. Consider testing for open relay or user enumeration.",
    "dns": "DNS service found. Could be vulnerable to zone transfer attacks (try 'dig axfr @<target> <domain>').",
    "mysql": "MySQL database found. Check for default credentials or vulnerabilities.",
    "postgres": "PostgreSQL database found. Check for default credentials.",
    "rdp": "Remote Desktop Protocol found. Check for weak credentials or vulnerabilities like BlueKeep."
}

def get_suggestion(service_string: str) -> str:
    """
    Analyzes a service string from Nmap and returns a suggested next step.

    Args:
        service_string: The full service description (e.g., "http", "ssl/http", "OpenSSH").

    Returns:
        A string containing a suggested action, or a default message if no match is found.
    """
    # Convert to lowercase for case-insensitive matching
    service_lower = service_string.lower()

    for keyword, suggestion in SUGGESTION_MAP.items():
        if keyword in service_lower:
            return suggestion
    
    # Default message if no specific keyword is found
    return "No specific suggestion. Investigate the service manually."

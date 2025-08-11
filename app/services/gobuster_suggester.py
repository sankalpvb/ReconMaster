# reconmaster/app/services/gobuster_suggester.py

# A dictionary for high-priority, sensitive path findings.
# We check if a keyword is IN the path string.
PATH_SUGGESTIONS = {
    ".git": "CRITICAL: Exposed Git repository. Use a tool like 'git-dumper' to download the source code.",
    ".env": "CRITICAL: Exposed environment file. This may contain API keys, database credentials, or other secrets.",
    "wp-admin": "Potential WordPress admin panel. Check for default credentials (admin/password) or run WPScan.",
    "admin": "Potential admin panel. Check for weak or default credentials.",
    "login": "Login page found. Consider testing for common vulnerabilities like SQL injection or weak passwords.",
    "dashboard": "Dashboard found. Attempt to access and check for authentication bypass vulnerabilities.",
    "config": "Configuration file or directory found. Investigate for sensitive information leakage.",
    "backup": "Backup file or directory found. May contain old source code or sensitive data."
}

# A dictionary mapping HTTP status codes to their meaning and a suggested action.
STATUS_SUGGESTIONS = {
    200: "OK. The resource is accessible. Investigate it for sensitive information or further enumeration.",
    204: "No Content. The server processed the request but there is no content to display. Might be an API endpoint.",
    301: "Moved Permanently. This path redirects to another location. Note the new URL and investigate it.",
    302: "Found (Redirect). This is a temporary redirect. Note the new location.",
    307: "Temporary Redirect. Similar to a 302, the resource has been moved temporarily.",
    401: "Unauthorized. Access is denied due to invalid credentials. This page may be behind a login.",
    403: "Forbidden. You do not have permission to access this. It might be possible to bypass this restriction.",
    404: "Not Found. The standard response for a non-existent page.",
    500: "Internal Server Error. The server encountered an error. This can sometimes leak information."
}

def get_suggestion(status_code: int, path: str) -> str:
    """
    Takes an HTTP status code and path, and returns a relevant suggestion.
    It prioritizes path-based suggestions over status-based ones.
    """
    path_lower = path.lower()

    # First, check for high-priority path keywords.
    for keyword, suggestion in PATH_SUGGESTIONS.items():
        if keyword in path_lower:
            return suggestion # Return the specific, high-value suggestion

    # If no path keyword is found, fall back to the status code suggestion.
    return STATUS_SUGGESTIONS.get(status_code, "No specific suggestion for this status code. Investigate manually.")

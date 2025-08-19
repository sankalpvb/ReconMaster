# reconmaster/app/services/gobuster_suggester.py

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

STATUS_SUGGESTIONS = {
    200: "OK. The resource is accessible. Investigate it for sensitive information or further enumeration.",
    301: "Moved Permanently. This path redirects to another location. Note the new URL and investigate it.",
    401: "Unauthorized. Access is denied due to invalid credentials. This page may be behind a login.",
    403: "Forbidden. You do not have permission to access this. It might be possible to bypass this restriction."
}

def get_suggestion(status_code: int, path: str) -> str:
    """
    Takes an HTTP status code and path, and returns a relevant suggestion.
    """
    path_lower = path.lower()
    for keyword, suggestion in PATH_SUGGESTIONS.items():
        if keyword in path_lower:
            return suggestion
    return STATUS_SUGGESTIONS.get(status_code, "No specific suggestion for this status code. Investigate manually.")

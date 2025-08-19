# reconmaster/app/services/whatweb_suggester.py

# A dictionary mapping keywords found in WhatWeb plugins to suggestions.
SUGGESTION_MAP = {
    "wordpress": "WordPress detected. Consider using a dedicated scanner like WPScan to enumerate plugins, themes, and users.",
    "joomla": "Joomla detected. Consider using a dedicated scanner like JoomScan to check for vulnerabilities.",
    "drupal": "Drupal detected. Check for known vulnerabilities for the specific version and consider using a tool like Droopescan.",
    "apache": "Apache web server detected. Check the specific version for known vulnerabilities using searchsploit.",
    "nginx": "Nginx web server detected. Check for common misconfigurations and the specific version for known vulnerabilities.",
    "iis": "Microsoft IIS web server detected. Often associated with Windows servers; check for ASP.NET vulnerabilities.",
    "jquery": "jQuery JavaScript library detected. Check the version number for known client-side vulnerabilities like XSS.",
    "php": "PHP is being used. Check the version (often in the X-Powered-By header) for known exploits.",
    "asp.net": "ASP.NET framework detected. Look for common .NET vulnerabilities like deserialization issues.",
    "cpanel": "cPanel login detected. This is a common hosting control panel; check for weak credentials.",
    "plesk": "Plesk login detected. This is a common hosting control panel; check for weak credentials."
}

def get_suggestion(plugin_name: str, result: str) -> str:
    """
    Analyzes a plugin and its result from WhatWeb and returns a suggestion.

    Args:
        plugin_name: The name of the WhatWeb plugin (e.g., "WordPress").
        result: The result of the plugin (e.g., "5.8.1").

    Returns:
        A string containing a suggested action, or a default message.
    """
    # Combine the plugin name and result for a comprehensive search
    search_string = f"{plugin_name} {result}".lower()

    for keyword, suggestion in SUGGESTION_MAP.items():
        if keyword in search_string:
            return suggestion
            
    # Default message if no specific keyword is found
    return "Technology identified. Research this specific technology and version for known vulnerabilities."

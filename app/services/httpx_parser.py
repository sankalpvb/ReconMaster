# reconmaster/app/services/httpx_parser.py

import re
from typing import List, Dict

def get_suggestion(tech_list: List[str]) -> str:
    """
    Analyzes a list of technologies and returns a relevant suggestion.
    For now, it provides a general suggestion, but this can be expanded.
    """
    if not tech_list:
        return "Live web server found. Investigate manually for technologies and vulnerabilities."
    
    # Join the list of technologies into a readable string
    tech_string = ", ".join(tech_list)
    return f"Technologies detected: {tech_string}. Research these for known vulnerabilities."

def parse_httpx_output(raw_output: str) -> List[Dict]:
    """
    Parses the raw text output from an httpx scan.
    
    Example line: http://example.com [200] [Example Domain] [Go,Netlify]
    """
    parsed_results = []
    
    # Regex to capture the URL, status code, title, and technologies
    # This is designed to be flexible and handle cases where parts are missing.
    line_regex = re.compile(r"^(https?://[^\s]+)\s+\[(\d{3})\]\s+\[([^\]]*)\]\s+\[([^\]]*)\]")

    for line in raw_output.splitlines():
        match = line_regex.match(line.strip())
        if match:
            url = match.group(1)
            status_code = int(match.group(2))
            title = match.group(3)
            # Technologies are comma-separated, so we split them into a list
            technologies = [tech.strip() for tech in match.group(4).split(',') if tech.strip()]
            
            suggestion = get_suggestion(technologies)

            host_info = {
                "url": url,
                "status": status_code,
                "title": title,
                "technologies": technologies, # Store as a list
                "suggestion": suggestion
            }
            parsed_results.append(host_info)
            
    return parsed_results

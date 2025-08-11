# reconmaster/app/services/gobuster_parser.py

import re
from typing import List, Dict

from . import gobuster_suggester

def parse_gobuster_output(raw_output: str) -> List[Dict]:
    """
    Parses the raw text output from a Gobuster scan to find discovered paths,
    status codes, and content length, then generates suggestions.
    """
    parsed_results = []
    
    # Regex to find lines like: /images (Status: 301) [Size: 178]
    # This is more robust and captures all three pieces of information.
    path_regex = re.compile(r"^(?:Found: )?(.+?)\s+\(Status: (\d{3})\)\s+\[Size: (\d+)\]")

    for line in raw_output.splitlines():
        match = path_regex.search(line.strip())
        if match:
            path = match.group(1).strip()
            status_code = int(match.group(2))
            size = int(match.group(3))

            # Get a suggestion for the found status code and path
            # Note: We will make the suggester smarter in the next step.
            suggestion = gobuster_suggester.get_suggestion(status_code, path)

            path_info = {
                "path": path,
                "status": status_code,
                "size": size,
                "suggestion": suggestion
            }
            if path_info not in parsed_results:
                parsed_results.append(path_info)
            
    return parsed_results

# reconmaster/app/services/gobuster_parser.py

import re
from typing import List, Dict
from . import gobuster_suggester

def parse_gobuster_output(raw_output: str) -> List[Dict]:
    """
    Parses Gobuster output. This version is robust and handles different
    output formats from the tool.
    """
    parsed_results = []
    path_regex = re.compile(r"^(.*?)\s+\(Status:\s*(\d{3})\)\s+\[Size:\s*(\d+)\]")

    for line in raw_output.splitlines():
        clean_line = re.sub(r'\x1b\[[0-9;]*m', '', line).strip()
        match = path_regex.search(clean_line)
        if match:
            path = match.group(1).strip()
            status_code = int(match.group(2))
            size = int(match.group(3))
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

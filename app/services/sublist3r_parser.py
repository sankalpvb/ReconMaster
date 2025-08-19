# reconmaster/app/services/sublist3r_parser.py

import re
from typing import List, Dict

from . import sublist3r_suggester

def parse_sublist3r_output(raw_output: str) -> List[Dict]:
    """
    Parses the raw text output from a Sublist3r scan to find discovered subdomains.
    """
    parsed_results = []
    
    # A simple regex to find lines that look like valid hostnames.
    # This is effective for Sublist3r's clean output.
    domain_regex = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$")

    # Keep track of found domains to avoid duplicates
    found_domains = set()

    for line in raw_output.splitlines():
        # Sublist3r sometimes includes ANSI color codes, so we clean them.
        clean_line = re.sub(r'\x1b\[[0-9;]*m', '', line).strip()
        
        if domain_regex.match(clean_line) and clean_line not in found_domains:
            suggestion = sublist3r_suggester.get_suggestion(clean_line)
            
            domain_info = {
                "subdomain": clean_line,
                "suggestion": suggestion
            }
            parsed_results.append(domain_info)
            found_domains.add(clean_line)
            
    return parsed_results

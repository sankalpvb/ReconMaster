# reconmaster/app/services/assetfinder_parser.py

import re
from typing import List, Dict

def get_suggestion(subdomain: str) -> str:
    """Returns a suggestion for a found subdomain."""
    return "Subdomain found. Consider running an Nmap scan on this host to discover open ports."

def parse_assetfinder_output(raw_output: str) -> List[Dict]:
    """
    Parses the raw text output from an assetfinder scan.
    """
    parsed_results = []
    found_domains = set()

    for line in raw_output.splitlines():
        # The output is just one domain per line, so we just need to clean it.
        clean_line = line.strip()
        if clean_line and clean_line not in found_domains:
            suggestion = get_suggestion(clean_line)
            
            domain_info = {
                "subdomain": clean_line,
                "suggestion": suggestion
            }
            parsed_results.append(domain_info)
            found_domains.add(clean_line)
            
    return parsed_results

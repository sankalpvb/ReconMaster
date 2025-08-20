# reconmaster/app/services/whois_parser.py
from typing import List, Dict

def parse_whois_output(raw_output: str) -> List[Dict]:
    """
    Parses the key-value output from a whois scan.
    """
    parsed_results = []
    for line in raw_output.splitlines():
        # Ensure the line contains a colon to be considered a key-value pair
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Add to results only if both key and value are not empty
            if key and value and ">>>" not in key:
                parsed_results.append({"key": key, "value": value})
    return parsed_results

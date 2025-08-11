# reconmaster/app/services/nmap_parser.py

import re
from typing import List, Dict

# Import our new suggestion engine
from . import suggestion_engine

def parse_nmap_output(raw_output: str) -> List[Dict]:
    """
    Parses the raw text output from an Nmap scan to find open ports
    and generate suggestions for next steps.
    """
    parsed_results = []
    
    # Regex to find lines like: 80/tcp open http
    port_regex = re.compile(r"^(\d+\/(?:tcp|udp))\s+([a-zA-Z]+)\s+([a-zA-Z0-9\-\/\?_]+.*)$")

    for line in raw_output.splitlines():
        match = port_regex.match(line.strip())
        if match:
            service = match.group(3).strip()
            
            # Get a suggestion for the found service
            suggestion = suggestion_engine.get_suggestion(service)

            port_info = {
                "port": match.group(1),
                "state": match.group(2),
                "service": service,
                "suggestion": suggestion # Add the new suggestion to our data
            }
            parsed_results.append(port_info)
            
    return parsed_results

# reconmaster/app/services/ffuf_parser.py
import re
from typing import List, Dict

def parse_ffuf_output(raw_output: str) -> List[Dict]:
    """
    Parses the ffuf output. This is a simplified parser; a real one
    would ideally use ffuf's JSON output for more reliability.
    """
    parsed_results = []
    # A simple regex to capture the path and status code from ffuf's output
    # This assumes a relatively standard output format.
    result_regex = re.compile(r"^([^\[\s]+)\s+\[Status: (\d{3})")

    for line in raw_output.splitlines():
        # Ignore comments and ffuf's progress/header lines
        if line.strip().startswith('#') or "Progress:" in line or "::" in line or "FUZZ" in line:
            continue
        
        match = result_regex.search(line.strip())
        if match:
            path = match.group(1).strip()
            status = match.group(2).strip()
            parsed_results.append({"path": path, "status": status})
            
    return parsed_results

# reconmaster/app/services/whatweb_parser.py

import re
from typing import List, Dict

# Import our suggestion engine
from . import whatweb_suggester

def parse_whatweb_output(raw_output: str) -> List[Dict]:
    """
    Parses the raw text output from a WhatWeb scan to find identified technologies
    and generate suggestions. This version is more robust and handles multi-line output,
    ANSI color codes, and prevents duplicates.
    """
    parsed_results = []
    # A set to keep track of added results to avoid duplicates
    seen_results = set()

    # Regex to find individual plugins like "PluginName[Result]"
    plugin_regex = re.compile(r"([\w-]+)\[([^\]]+)\]")
    
    # Regex to remove ANSI color codes
    ansi_escape_regex = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    for line in raw_output.splitlines():
        # Clean the line of any color codes
        clean_line = ansi_escape_regex.sub('', line)

        # Find all plugin matches on the current line
        matches = plugin_regex.findall(clean_line)
        for match in matches:
            plugin_name = match[0].strip()
            plugin_result = match[1].strip()
            
            # Create a unique key to prevent duplicate entries (e.g., "Country:UNITED STATES")
            result_key = f"{plugin_name}:{plugin_result}"

            if result_key not in seen_results:
                # Get a suggestion for the found technology
                suggestion = whatweb_suggester.get_suggestion(plugin_name, plugin_result)

                plugin_info = {
                    "plugin": plugin_name,
                    "result": plugin_result,
                    "suggestion": suggestion
                }
                parsed_results.append(plugin_info)
                seen_results.add(result_key)
            
    return parsed_results

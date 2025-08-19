# reconmaster/app/services/executor.py

import asyncio
import subprocess
import importlib
import json

# Import all of our parsers
from . import nmap_parser
from . import gobuster_parser
from . import assetfinder_parser
from . import sublist3r_parser
from . import whatweb_parser

COMMAND_MAP = {
    "Nmap": "nmap",
    "Gobuster": "gobuster",
    "Assetfinder": "assetfinder",
    "Sublist3r": "sublist3r",
    "WhatWeb": "whatweb"
}

# Helper coroutine to read a stream (no changes)
async def _stream_reader(stream, websocket, output_list, is_stderr=False):
    while True:
        line_bytes = await stream.readline()
        if not line_bytes:
            break
        line = line_bytes.decode().strip()
        output_list.append(line)
        prefix = "ERROR: " if is_stderr else ""
        await websocket.send_text(prefix + line)

async def run_command_stream(tool_name: str, target: str, options: str, websocket):
    if tool_name not in COMMAND_MAP:
        await websocket.send_text(f"ERROR: Tool '{tool_name}' is not a valid or allowed tool.")
        return

    try:
        module_name = f"app.tools.{tool_name.lower()}_tool"
        tool_module = importlib.import_module(module_name)
        command = tool_module.build_command(target, options)
    except ImportError:
        await websocket.send_text(f"ERROR: No execution logic found for tool '{tool_name}'.")
        return
    except Exception as e:
        await websocket.send_text(f"ERROR: Could not build command for {tool_name}: {e}")
        return

    await websocket.send_text(f"INFO: Running command: {' '.join(command)}\n\n")

    try:
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        full_output_list = []

        await asyncio.gather(
            _stream_reader(process.stdout, websocket, full_output_list),
            _stream_reader(process.stderr, websocket, full_output_list, is_stderr=True)
        )

        await process.wait()
        exit_code = process.returncode
        full_output = "\n".join(full_output_list)

        # --- MODIFIED: PARSING LOGIC WITH DEBUGGING ---
        print(f"--- DEBUG: Scan finished for tool: {tool_name} ---") # DEBUG MESSAGE
        parsed_data = None
        if tool_name == "Nmap":
            parsed_data = nmap_parser.parse_nmap_output(full_output)
        elif tool_name == "Gobuster":
            parsed_data = gobuster_parser.parse_gobuster_output(full_output)
        elif tool_name == "Assetfinder":
            print("--- DEBUG: Entering Assetfinder parsing logic ---") # DEBUG MESSAGE
            parsed_data = assetfinder_parser.parse_assetfinder_output(full_output)
            print(f"--- DEBUG: Assetfinder parser returned: {parsed_data} ---") # DEBUG MESSAGE
        elif tool_name == "Sublist3r":
            parsed_data = sublist3r_parser.parse_sublist3r_output(full_output)
        elif tool_name == "WhatWeb":
            parsed_data = whatweb_parser.parse_whatweb_output(full_output)

        if parsed_data:
            print("--- DEBUG: Parsed data found, sending to frontend. ---") # DEBUG MESSAGE
            await websocket.send_text(json.dumps({
                "type": "parsed_data",
                "tool": tool_name,
                "data": parsed_data
            }))
        else:
            print("--- DEBUG: No parsed data found. Nothing to send. ---") # DEBUG MESSAGE

        await websocket.send_text(f"\n\nINFO: Process finished with exit code {exit_code}.")

    except FileNotFoundError:
        base_command = COMMAND_MAP.get(tool_name, "unknown")
        await websocket.send_text(f"ERROR: Command '{base_command}' not found. Is {tool_name} installed?")
    except Exception as e:
        await websocket.send_text(f"ERROR: An unexpected error occurred during execution: {str(e)}")

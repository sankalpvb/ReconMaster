# reconmaster/app/services/executor.py
import asyncio
import subprocess
import importlib
import json

# Import all parsers, including the new ones
from . import nmap_parser
from . import gobuster_parser
from . import assetfinder_parser
from . import sublist3r_parser
from . import whatweb_parser
from . import httpx_parser
from . import ffuf_parser
from . import whois_parser

COMMAND_MAP = {
    "Nmap": "nmap",
    "Gobuster": "gobuster",
    "Assetfinder": "assetfinder",
    "Sublist3r": "sublist3r",
    "WhatWeb": "whatweb",
    "httpx": "httpx",
    "ffuf": "ffuf",
    "whois": "whois"
    # Add all other tool names here as they are created
}

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
    except Exception as e:
        await websocket.send_text(f"ERROR: Could not build command for {tool_name}: {e}")
        return

    await websocket.send_text(f"INFO: Running command: {' '.join(command)}\n\n")

    try:
        # For tools that take input via stdin (like httpx with a list)
        stdin_input = None
        if tool_name == "httpx":
            stdin_input = target.encode('utf-8')

        process = await asyncio.create_subprocess_exec(
            *command,
            stdin=subprocess.PIPE if stdin_input else None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if stdin_input:
            process.stdin.write(stdin_input)
            await process.stdin.drain()
            process.stdin.close()

        full_output_list = []
        await asyncio.gather(
            _stream_reader(process.stdout, websocket, full_output_list),
            _stream_reader(process.stderr, websocket, full_output_list, is_stderr=True)
        )

        await process.wait()
        exit_code = process.returncode
        full_output = "\n".join(full_output_list)

        # --- The complete parsing logic ---
        parsed_data = None
        if tool_name == "Nmap": parsed_data = nmap_parser.parse_nmap_output(full_output)
        elif tool_name == "Gobuster": parsed_data = gobuster_parser.parse_gobuster_output(full_output)
        elif tool_name == "Assetfinder": parsed_data = assetfinder_parser.parse_assetfinder_output(full_output)
        elif tool_name == "Sublist3r": parsed_data = sublist3r_parser.parse_sublist3r_output(full_output)
        elif tool_name == "WhatWeb": parsed_data = whatweb_parser.parse_whatweb_output(full_output)
        elif tool_name == "httpx": parsed_data = httpx_parser.parse_httpx_output(full_output)
        elif tool_name == "ffuf": parsed_data = ffuf_parser.parse_ffuf_output(full_output)
        elif tool_name == "whois": parsed_data = whois_parser.parse_whois_output(full_output)

        if parsed_data:
            await websocket.send_text(json.dumps({
                "type": "parsed_data", "tool": tool_name, "data": parsed_data
            }))

        await websocket.send_text(f"\n\nINFO: Process finished with exit code {exit_code}.")

    except FileNotFoundError:
        await websocket.send_text(f"ERROR: Command '{COMMAND_MAP.get(tool_name)}' not found.")
    except Exception as e:
        await websocket.send_text(f"ERROR: An unexpected error occurred: {str(e)}")

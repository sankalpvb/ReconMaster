# reconmaster/app/services/executor.py

import asyncio
import subprocess
import importlib
import json

from . import nmap_parser

COMMAND_MAP = {
    "Nmap": "nmap",
    "Gobuster": "gobuster",
    "Sublist3r": "sublist3r",
    "WhatWeb": "whatweb"
}

# Helper coroutine to read a stream and send data over the websocket
async def _stream_reader(stream, websocket, output_list, is_stderr=False):
    while True:
        line_bytes = await stream.readline()
        if not line_bytes:
            break
        line = line_bytes.decode().strip()
        output_list.append(line) # Add line to the list for later parsing
        prefix = "ERROR: " if is_stderr else ""
        await websocket.send_text(prefix + line)

async def run_command_stream(tool_name: str, target: str, options: str, websocket):
    """
    Dynamically loads a tool module, builds its command, streams its output,
    and sends a final parsed summary.
    """
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

        full_output_list = [] # Use a list to collect all output lines

        # Concurrently read stdout and stderr until both streams are closed
        await asyncio.gather(
            _stream_reader(process.stdout, websocket, full_output_list),
            _stream_reader(process.stderr, websocket, full_output_list, is_stderr=True)
        )

        # Wait for the process to fully terminate
        await process.wait()
        exit_code = process.returncode

        # Join the collected lines into a single string for parsing
        full_output = "\n".join(full_output_list)

        # After the process finishes, parse the collected output
        if tool_name == "Nmap":
            parsed_data = nmap_parser.parse_nmap_output(full_output)
            if parsed_data:
                # Send the structured data in a special JSON message
                await websocket.send_text(json.dumps({
                    "type": "parsed_data",
                    "tool": "Nmap",
                    "data": parsed_data
                }))

        await websocket.send_text(f"\n\nINFO: Process finished with exit code {exit_code}.")

    except FileNotFoundError:
        base_command = COMMAND_MAP.get(tool_name, "unknown")
        await websocket.send_text(f"ERROR: Command '{base_command}' not found. Is {tool_name} installed?")
    except Exception as e:
        await websocket.send_text(f"ERROR: An unexpected error occurred during execution: {str(e)}")


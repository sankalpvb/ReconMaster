# reconmaster/app/api/routes.py

import json
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from typing import List

from ..db import models
from ..db.database import SessionLocal
from . import schemas
from ..services import executor

router = APIRouter()

# Dependency to get a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Tool Endpoints ---

def get_tool(db: Session, tool_id: int):
    tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    if tool is None:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool

@router.get("/tools", response_model=List[schemas.Tool])
def get_all_tools(db: Session = Depends(get_db)):
    tools = db.query(models.Tool).all()
    return tools

@router.get("/tools/{tool_id}", response_model=schemas.Tool)
def get_tool_by_id(tool_id: int, db: Session = Depends(get_db)):
    return get_tool(db=db, tool_id=tool_id)


# --- Scan Result Endpoints ---

@router.post("/scans", response_model=schemas.ScanResult)
def create_scan_result(scan: schemas.ScanResultCreate, db: Session = Depends(get_db)):
    """
    Save a new scan result to the database.
    """
    db_scan_result = models.ScanResult(**scan.model_dump())
    db.add(db_scan_result)
    db.commit()
    db.refresh(db_scan_result)
    return db_scan_result

@router.get("/scans", response_model=List[schemas.ScanResult])
def get_all_scan_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all saved scan results (scan history).
    """
    # Order by most recent first
    scans = db.query(models.ScanResult).order_by(models.ScanResult.timestamp.desc()).offset(skip).limit(limit).all()
    return scans

@router.get("/scans/{scan_id}", response_model=schemas.ScanResult)
def get_scan_result_by_id(scan_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a specific saved scan.
    """
    scan = db.query(models.ScanResult).filter(models.ScanResult.id == scan_id).first()
    if scan is None:
        raise HTTPException(status_code=404, detail="Scan result not found")
    return scan


# --- WebSocket Endpoint ---
@router.websocket("/ws/run/{tool_id}")
async def websocket_endpoint(websocket: WebSocket, tool_id: int, db: Session = Depends(get_db)):
    await websocket.accept()
    try:
        tool = get_tool(db=db, tool_id=tool_id)
        payload_str = await websocket.receive_text()
        payload = json.loads(payload_str)
        
        target = payload.get("target")
        options = payload.get("options", "")

        if not target:
            await websocket.send_text("ERROR: Target not provided.")
            return

        await websocket.send_text(f"INFO: Received target '{target}' with options '{options}' for tool '{tool.name}'. Starting process...")

        await executor.run_command_stream(
            tool_name=tool.name,
            target=target,
            options=options,
            websocket=websocket
        )

    except WebSocketDisconnect:
        print(f"Client disconnected.")
    except json.JSONDecodeError:
        print("Error decoding JSON from client.")
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        try:
            await websocket.send_text(f"ERROR: {error_message}")
        except RuntimeError:
            pass
    finally:
        if websocket.client_state != "DISCONNECTED":
             await websocket.close()

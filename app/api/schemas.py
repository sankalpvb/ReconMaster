# reconmaster/app/api/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime # ADD THIS IMPORT

# This is the Pydantic model (schema) for our Tool data.
# It defines the shape of the data that will be sent over the API.

class ToolBase(BaseModel):
    name: str
    category: str
    description: str
    base_command: str
    advantages: Optional[str] = None
    example_usage: Optional[str] = None

class Tool(ToolBase):
    id: int

    class Config:
        # This tells Pydantic to read the data even if it is not a dict,
        # but an ORM model (like our SQLAlchemy Tool model).
        from_attributes = True


# --- NEW: Schemas for Scan Results ---

# Schema for creating a new scan result (what the frontend will send)
class ScanResultCreate(BaseModel):
    tool_id: int
    target: str
    options: Optional[str] = None
    output: str

# Schema for reading a scan result (what the API will return)
class ScanResult(ScanResultCreate):
    id: int
    timestamp: datetime
    tool: Tool # Include the full tool details in the response

    class Config:
        from_attributes = True

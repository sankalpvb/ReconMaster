# reconmaster/app/db/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime # MODIFIED
from sqlalchemy.orm import relationship # MODIFIED
from datetime import datetime # MODIFIED
from .database import Base

# The Tool model remains the same
class Tool(Base):
    __tablename__ = "tools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    category = Column(String, index=True)
    description = Column(Text, nullable=False)
    base_command = Column(String, nullable=False)
    advantages = Column(Text) 
    example_usage = Column(String)

    # This creates a relationship between Tool and ScanResult
    scan_results = relationship("ScanResult", back_populates="tool")


# --- NEW: ScanResult Model ---
# This table will store the output of every saved scan.
class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True, index=True)
    tool_id = Column(Integer, ForeignKey("tools.id")) # Foreign key to link to the tools table
    target = Column(String, nullable=False)
    options = Column(String)
    output = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # This completes the relationship
    tool = relationship("Tool", back_populates="scan_results")

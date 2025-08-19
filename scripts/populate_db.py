# reconmaster/scripts/populate_db.py

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.db.database import SessionLocal, engine
from app.db.models import Tool, Base

def populate_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        db.query(Tool).delete()
        db.commit()
        print("Cleared old tools from the database.")
        print("Populating database with updated tools...")

        tools_to_add = [
            Tool(name="Nmap", category="Network Scanner", description="A powerful tool for network discovery and security auditing.", base_command="nmap", advantages="Extremely versatile, scriptable engine (NSE).", example_usage="nmap -sV -T4 example.com"),
            Tool(name="Gobuster", category="Web Content Discovery", description="A tool used to brute-force URIs (directories and files).", base_command="gobuster dir", advantages="Very fast, simple to use, supports multiple modes.", example_usage="gobuster dir -u http://example.com -w <wordlist>"),
            Tool(name="Assetfinder", category="Subdomain Enumeration", description="A fast and simple tool for finding subdomains related to a given domain.", base_command="assetfinder", advantages="Extremely fast, lightweight, and aggregates data from many sources.", example_usage="assetfinder --subs-only example.com"),
            # --- RESTORED Sublist3r ---
            Tool(name="Sublist3r", category="Subdomain Enumeration", description="Enumerates subdomains of websites using OSINT from multiple search engines.", base_command="sublist3r", advantages="Aggregates results from many sources like Google, Yahoo, and VirusTotal.", example_usage="sublist3r -d example.com"),
            Tool(name="WhatWeb", category="Website Fingerprinting", description="Identifies web technologies including CMS, JavaScript libraries, and web servers.", base_command="whatweb", advantages="Highly detailed output, plugin-based architecture.", example_usage="whatweb example.com")
        ]
        db.add_all(tools_to_add)
        db.commit()
        print("Database successfully populated with both Assetfinder and Sublist3r!")
    finally:
        db.close()

if __name__ == "__main__":
    populate_db()

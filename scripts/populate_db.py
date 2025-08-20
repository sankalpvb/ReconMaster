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
        print("Populating database with the full tool roadmap...")

        # --- List of all tools to be added, categorized ---
        tools_to_add = [
            # --- Active & Complete Tools ---
            Tool(name="Nmap", category="Network Scanning", description="A powerful tool for network discovery and security auditing.", base_command="nmap"),
            Tool(name="Gobuster", category="Web Enumeration", description="A tool used to brute-force URIs (directories and files).", base_command="gobuster"),
            Tool(name="Assetfinder", category="Subdomain & DNS Enumeration", description="A fast and simple tool for finding subdomains related to a given domain.", base_command="assetfinder"),
            Tool(name="Sublist3r", category="Subdomain & DNS Enumeration", description="Enumerates subdomains of websites using OSINT from multiple search engines.", base_command="sublist3r"),
            Tool(name="WhatWeb", category="Technology Fingerprinting", description="Identifies web technologies including CMS, JavaScript libraries, and web servers.", base_command="whatweb"),
	    Tool(name="httpx", category="Web Enumeration", description="Identifies web technologies including CMS, JavaScript libraries, and web servers.", base_command="httpx"),
            # --- Future Tools (Inactive) ---
            Tool(name="whois", category="Information Gathering", description="Find domain ownership information.", base_command="whois"),
            Tool(name="theHarvester", category="Information Gathering", description="Gather emails, subdomains, and hosts from public sources.", base_command="theHarvester"),
            Tool(name="amass", category="Subdomain & DNS Enumeration", description="In-depth DNS enumeration and network mapping.", base_command="amass"),
            Tool(name="masscan", category="Network Scanning", description="Extremely fast port scanner for large networks.", base_command="masscan"),
            Tool(name="ffuf", category="Web Enumeration", description="Fast web fuzzer written in Go.", base_command="ffuf"),
            Tool(name="nikto", category="Web Enumeration", description="Web server scanner which performs comprehensive tests.", base_command="nikto"),
            Tool(name="enum4linux-ng", category="Service Enumeration", description="A next generation SMB enumeration tool.", base_command="enum4linux-ng"),
            Tool(name="dnsrecon", category="Subdomain & DNS Enumeration", description="Powerful DNS enumeration script.", base_command="dnsrecon"),
            Tool(name="eyewitness", category="Visualization", description="Take screenshots of web pages to provide visual context.", base_command="eyewitness")
        ]
        
        db.add_all(tools_to_add)
        db.commit()
        print("Database successfully populated with the full toolset!")
    finally:
        db.close()

if __name__ == "__main__":
    populate_db()

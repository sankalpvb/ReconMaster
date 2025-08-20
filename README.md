# ReconMaster 🚀  
**An Intelligent Web-based Reconnaissance Framework for Security Professionals**  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-red.svg)](https://fastapi.tiangolo.com/)  
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)](https://www.sqlite.org/)  

---
## 🎯 Introduction  

ReconMaster is a Python-powered web application that provides a clean, interactive, and intelligent front-end for a suite of powerful command-line security tools.  

It streamlines the reconnaissance phase of a security assessment by:  
- Running scans  
- Parsing raw terminal output into structured results  
- Offering actionable suggestions for next steps  

This transforms the complex and ephemeral nature of reconnaissance into a **structured, persistent, and insightful workflow**.  

---

## ✨ Key Features  

- **Centralized Web UI:** Dark/light theme with an intuitive layout.  
- **Real-time Output:** View command results as they are generated.  
- **Intelligent Parsing Engine:** Extracts open ports, directories, subdomains, and technologies into tables.  
- **"Always-On" Suggestion Engine:** Provides context-aware recommendations (including Exploit-DB lookups).  
- **Persistent Scan History:** Save and review past scans via a history page.  
- **Interactive Controls:** Cancel scans, click discovered links, and toggle themes.  
- **Modular & Scalable:** Easily add new tools to the framework.  

---

## 🛠️ Technology Stack  

- **Backend:** Python 3, FastAPI, Uvicorn  
- **Real-time:** WebSockets  
- **Database:** SQLite + SQLAlchemy ORM  
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (ES6 Modules)  
- **UI Framework:** Bootstrap 5  
- **Core Logic:** Python’s `asyncio` + `subprocess`  
- **Integrated Tools:**  
  - Nmap  
  - Gobuster  
  - Assetfinder  
  - Sublist3r  
  - WhatWeb  
  - `searchsploit` (Exploit-DB)  
  - httpx  
  - ffuf  
  - whois  
  - nikto  

---

## ⚙️ Setup and Installation  

ReconMaster comes with an **automated setup script**.  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/sankalpvb/ReconMaster.git
   cd ReconMaster
  

2. **Make the setup script executable:**

   ```bash
   chmod +x setup.sh
   ```

3. **Run the setup script (with sudo):**

   ```bash
   sudo ./setup.sh
   ```

   * Installs required system tools (Nmap, Gobuster, etc.)
   * Optionally installs **Exploit-DB** (large package)
   * Installs `httpx` via Go
   * Creates Python virtual environment
   * Installs dependencies from `requirements.txt`
   * Initializes the SQLite database

---

## 📖 Usage

Once setup is complete, follow these steps:

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

2. **Start the server:**

   ```bash
   uvicorn app.main:app --reload
   ```

3. **Open your browser:**
   Go to **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

From the UI:

* Select a tool from the sidebar
* Enter your target and configure options
* Click **"Initiate Scan"**
* View results in the **Analysis Table** and **Raw Output log**
* Save results to **History** for later review

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```

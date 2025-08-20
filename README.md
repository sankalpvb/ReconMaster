# ReconMaster 🚀  
**An Intelligent Web-based Reconnaissance Framework for Security Professionals**  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-red.svg)](https://fastapi.tiangolo.com/)  
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)](https://www.sqlite.org/)  

ReconMaster provides a modern browser-based UI for managing cybersecurity reconnaissance tools. It streamlines the reconnaissance phase of security assessments by running scans, parsing results into structured outputs, and offering actionable next steps.  

---

## ✨ Features  
- **Centralized Web UI** – Dark/light theme with intuitive layout.  
- **Real-time Scan Output** – Live logs via WebSockets.  
- **Intelligent Parsing** – Extracts ports, directories, subdomains, and technologies.  
- **Exploit Suggestions** – Optional Exploit-DB (`searchsploit`) integration.  
- **Scan History** – Save and review past results.  
- **Interactive Controls** – Cancel scans, click results, toggle themes.  
- **Extensible** – Add new tools easily.  

---

## ⚙️ Quick Setup  

The project comes with a **fully automated setup script**.  

```bash
# Clone repository
git clone https://github.com/sankalpvb/ReconMaster.git
cd ReconMaster

# Make the setup script executable
chmod +x setup.sh

# Run setup with sudo
sudo ./setup.sh
````

The script will:

* Install system dependencies (Nmap, Gobuster, Sublist3r, WhatWeb, etc.)
* Optionally install Exploit-DB (`searchsploit`)
* Install `httpx` (via Go)
* Set up Python virtual environment & dependencies
* Initialize the SQLite database

---

## ▶️ Running ReconMaster

After setup:

```bash
# Activate virtual environment
source venv/bin/activate

# Start the server
uvicorn app.main:app --reload
```

Open your browser at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📖 Usage

1. Select a tool from the sidebar.
2. Configure target and options.
3. Click **Initiate Scan**.
4. View results in **Analysis Table** (parsed) + **Raw Output**.
5. Save results to history for later review.
6. Access past scans via **Scan History**.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```
it strictly script-based?
```

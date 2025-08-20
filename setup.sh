#!/bin/bash

# ==============================================================================
# ReconMaster Setup Script
#
# This script automates the full setup process for the ReconMaster application.
# It checks for and installs system dependencies, sets up the Python virtual
# environment, installs required packages, and initializes the database.
#
# Usage:
# 1. Place this script in the root directory of the ReconMaster project.
# 2. Make it executable: chmod +x setup.sh
# 3. Run with sudo: sudo ./setup.sh
# ==============================================================================

# --- Color Codes for Output ---
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# --- Helper Function for Status Messages ---
function print_status {
    echo -e "\n${YELLOW}>> $1${NC}"
}

# --- 1. Check for Root/Sudo Privileges ---
print_status "Checking for root privileges..."
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}This script must be run as root. Please use 'sudo ./setup.sh'${NC}" 
   exit 1
fi
echo -e "${GREEN}Root privileges confirmed.${NC}"

# --- 2. Update System Package Lists ---
print_status "Updating package lists..."
apt update

# --- 3. Install System-Level Dependencies ---
print_status "Checking and installing system dependencies..."

# List of required system packages (ExploitDB is handled separately)
SYSTEM_PACKAGES=(
    nmap
    gobuster
    assetfinder
    whatweb
    sublist3r
    ffuf
    whois
    nikto
    python3-pip
    python3-venv
    golang-go
)

for pkg in "${SYSTEM_PACKAGES[@]}"; do
    if command -v $pkg &> /dev/null; then
        echo -e "${GREEN}- $pkg is already installed.${NC}"
    else
        echo -e "${YELLOW}- $pkg not found. Installing...${NC}"
        apt install -y $pkg
    fi
done

# --- NEW: Optional ExploitDB Installation ---
print_status "Optional Dependency: Exploit-DB"
if command -v searchsploit &> /dev/null; then
    echo -e "${GREEN}- Exploit-DB (searchsploit) is already installed.${NC}"
else
    # Ask the user if they want to install it
    read -p "Do you want to install Exploit-DB (searchsploit)? It's a large package (~400MB) but enables specific exploit suggestions in Nmap. (y/n): " choice
    case "$choice" in 
      y|Y ) 
        echo -e "${YELLOW}- Installing Exploit-DB...${NC}"
        apt install -y exploitdb
        ;;
      n|N ) 
        echo -e "${YELLOW}- Skipping Exploit-DB installation.${NC}"
        ;;
      * ) 
        echo -e "${RED}- Invalid choice. Skipping Exploit-DB installation.${NC}"
        ;;
    esac
fi


# --- 4. Install ProjectDiscovery's httpx (Go-based) ---
print_status "Checking and installing ProjectDiscovery's httpx..."
if ! command -v /root/go/bin/httpx &> /dev/null; then
    echo -e "${YELLOW}- httpx not found. Installing via Go...${NC}"
    go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
    if [[ ! ":$PATH:" == *":/root/go/bin:"* ]]; then
        echo 'export PATH=$PATH:/root/go/bin' >> /root/.bashrc
        source /root/.bashrc
    fi
else
    echo -e "${GREEN}- httpx is already installed.${NC}"
fi


# --- 5. Install System-Wide Python Dependencies ---
print_status "Installing required system-wide Python packages..."
pip3 install requests --break-system-packages

# --- 6. Set Up Python Virtual Environment ---
print_status "Setting up Python virtual environment..."
VENV_DIR="venv"
if [ -d "$VENV_DIR" ]; then
    echo -e "${GREEN}- Virtual environment '$VENV_DIR' already exists.${NC}"
else
    echo -e "${YELLOW}- Creating virtual environment '$VENV_DIR'...${NC}"
    python3 -m venv $VENV_DIR
fi

# --- 7. Install Project-Specific Python Packages ---
print_status "Installing Python packages from requirements.txt..."
./$VENV_DIR/bin/pip install -r requirements.txt

# --- 8. Initialize the Database ---
print_status "Initializing the database..."
./$VENV_DIR/bin/python scripts/populate_db.py

# --- 9. Final Instructions ---
print_status "Setup Complete!"
echo -e "${GREEN}ReconMaster has been successfully installed.${NC}"
echo -e "\nTo run the application:"
echo -e "1. Activate the virtual environment: ${YELLOW}source venv/bin/activate${NC}"
echo -e "2. Start the server: ${YELLOW}uvicorn app.main:app --reload${NC}"
echo -e "3. Open your browser and go to ${YELLOW}http://127.0.0.1:8000${NC}"

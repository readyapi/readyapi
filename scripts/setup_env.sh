#!/bin/bash

# Documentation Migration Setup Script
# This script sets up a Python virtual environment and installs required dependencies

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== Setting up Documentation Migration Environment ===${NC}\n"

# Check for Python 3.8+
PYTHON_VERSION=$(python3 -c "import sys; print('{}.{}'.format(sys.version_info.major, sys.version_info.minor))")
PYTHON_VERSION_NUM=$(python3 -c "import sys; print('{}{:02d}'.format(sys.version_info.major, sys.version_info.minor))")
if [ "$PYTHON_VERSION_NUM" -lt 308 ]; then
    echo -e "${YELLOW}Python 3.8 or higher is required. Found Python $PYTHON_VERSION${NC}"
    exit 1
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo -e "${GREEN}Creating Python virtual environment...${NC}"
    python3 -m venv venv
    source venv/bin/activate

    # Upgrade pip
    pip install --upgrade pip

    # Install dependencies
    echo -e "\n${GREEN}Installing Python dependencies...${NC}"
    pip install -r requirements.txt

    echo -e "\n${GREEN}Environment setup complete!${NC}"
    echo -e "To activate the virtual environment, run: ${YELLOW}source venv/bin/activate${NC}"
else
    echo -e "${GREEN}Virtual environment already exists.${NC}"
    echo -e "To activate it, run: ${YELLOW}source venv/bin/activate${NC}"
fi

echo -e "\n${GREEN}Next steps:${NC}"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the migration script: python scripts/migrate_docs.py"
echo "3. Validate the documentation: python scripts/validate_docs.py"

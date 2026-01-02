#!/usr/bin/env bash

# Exit immediately if a command fails
set -e

echo "Activating virtual environment..."

# Activate venv (Linux / CI compatible)
source venv/bin/activate

echo "Running test suite..."

# Run pytest
pytest

echo "All tests passed ✅"

# Explicit success exit code
exit 0

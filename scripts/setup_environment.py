"""Setup environment and install packages with poetry."""

import os

try:
    # Update / Create poetry local poetry config to use isolated venv
    os.system("poetry config virtualenvs.create true --local")
    os.system("poetry config virtualenvs.in-project true --local")
    # Install dependencies
    os.system("poetry install")
except Exception as e:
    print("Could not setup venv or install packages with poetry.", e, e.__dict__)

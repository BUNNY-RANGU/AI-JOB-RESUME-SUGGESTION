import subprocess
import sys
import os

# Install dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Run Streamlit
os.execlp("streamlit", "streamlit", "run", "frontend/app.py", "--server.port=3000", "--server.address=0.0.0.0")

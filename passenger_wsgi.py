import sys
import os

# Add the backend directory to the system path so the app can be found
sys.path.insert(0, '/home/safynyrx/public_html/pr/backend')

# Import your Flask (or other framework) app from main.py
from main import app as application

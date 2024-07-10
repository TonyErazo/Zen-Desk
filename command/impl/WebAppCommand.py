from command.Command import Command

import subprocess
import os
import sys
from pathlib import Path

class WebAppCommand(Command):

    def __init__(self):
        Command.__init__(self, "/webapp")

    def execute(self):
        print("Loading web-app...")

        script_path = str(Path(__file__).parent.parent.parent) + str(os.path.join('\webapp', 'WebApp.py'))
        print(script_path)
        process = subprocess.run([sys.executable, '-m', 'streamlit', 'run', script_path])


        
        

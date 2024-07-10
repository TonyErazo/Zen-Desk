from command.Command import Command
import os
from pathlib import Path  

class ListCommand(Command):

    def __init__(self):
        Command.__init__(self, "/ls")

    def execute(self):
        print("Listing files...")

        file_path = Path(__file__).parent / '../../data/tickets/'
        dir_list = os.listdir(file_path)
        print(dir_list)

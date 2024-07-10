from command.Command import Command
import os
import csv
import pandas as pd
from pathlib import Path
from tabulate import tabulate

class ViewCommand(Command):

    def __init__(self):
        Command.__init__(self, "/view")

    def execute(self):
        ticket_name = "datafile.csv"
        file_path = Path(__file__).parent / '..\\..\\data\\tickets\\'  # Corrected path format
        target_file = str(file_path) + "\\" + ticket_name
        df = pd.read_csv(target_file, sep=",")

        print("Fetching tickets: " + target_file + "...")
        
        if os.path.exists(target_file) and os.path.isfile(target_file):
            self.view_ticket(target_file)

    def view_ticket(self, file):
        with open(file, 'r+', newline='') as input_file:
            df = pd.read_csv(file, sep=",")
            print(tabulate(df, headers='keys', tablefmt='psql'))
            print("\n")
from abc import ABC

from command.Command import Command
import random
import csv
import os
import pandas as pd
from pathlib import Path  


class SubmitCommand(Command):

    def __init__(self):
        Command.__init__(self, "/submit")
        self.file_name = "datafile.csv"
        self.file_path = Path(__file__).parent / '..\..\data\\tickets\\'
        self.file = Path(str(self.file_path) + "\\" + self.file_name)

    def execute(self):
        ticket_name = input("Please enter a name for the ticket\n")

        while True:

            ticket_priority = input("Please enter a ticket priority (High, Medium, Low)\n")

            if ticket_priority.lower() == "high" or ticket_priority.lower() == "medium" or ticket_priority.lower() == "low":
                ticket_priority.capitalize()
                break
            else:
                print("Please enter a valid value")

        ticket_description = input("Please enter a description for the ticket\n")

        # ticket_id = random.randint(0, 1000)
        # ticket_name = "ticket" + "-" + str(ticket_id)
        ticket_id = 0

        # print("dir: " + str(file_path))
        print("Your ticket has been generated name: " + self.file_name + " id: " + str(ticket_id))
        # print("created in the following path: " + str(file_path) + "\\" + ticket_name + '.csv')

        
        self.submit(ticket_name, ticket_priority, ticket_description)
              
        
    def submit(self, ticket_name, ticket_priority, ticket_description):

        if not self.file_path.is_dir():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file.is_file():
            # With will auto close the file
            with open(self.file, 'w', newline='') as input_file:
                print("Error: base file does not exist, a new one has been generated")
                writer = csv.writer(input_file)
                field = ["id", "name", "priority", "description"]
                
                writer.writerow(field)
                writer.writerow([ticket_id , ticket_name, ticket_priority, ticket_description])
        else:
            try:
                df = pd.read_csv(self.file, sep=",")
            except pd.errors.EmptyDataError:
                print("Empty csv error!")
                with open(self.file, 'w', newline='') as input_file:
                    writer = csv.writer(input_file)
                    field = ["id", "name", "priority", "description"]
                    
                    writer.writerow(field)
                    writer.writerow([ticket_id , ticket_name, ticket_priority, ticket_description])
                    input_file.close()
            

            ticket_id = int(df.iloc[-1:]['id'].iloc[0]) + 1

            df.loc[-1] = [ticket_id, ticket_name, ticket_priority, ticket_description]
            df.to_csv(self.file, index = False)
            return df
            # print("ticket id: " + str(ticket_id))

        


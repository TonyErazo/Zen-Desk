
from command.Command import Command

import os
import csv
import pandas as pd 
from pathlib import Path  
from command.impl.ViewCommand import ViewCommand

class EditCommand(Command):
    
    def __init__(self):
        Command.__init__(self, "/edit")
        self.view_command = ViewCommand()
        self.editing_ticket = True

    
    def execute(self):
        ticket_name = "datafile.csv"
        file_path = Path(__file__).parent / '..\..\data\\tickets\\'
        target_file = str(file_path) + "\\" + ticket_name

        print("Fetching tickets: " + target_file + "...")

        if os.path.exists(target_file) and os.path.isfile(target_file):
            self.view_command.view_ticket(target_file)
            self.edit_ticket(target_file)
    

    def edit_ticket(self, file):

        df = pd.read_csv(file, sep=",")
        while self.editing_ticket:
            
            ticket_id = input("Please enter the ticket id you'd like to edit. (Type exit to leave this menu)\n")

            if ticket_id.isnumeric():
                selected = df[df['id'] == int(ticket_id)]

                if not selected.empty:
                    print(selected)
                    while True:
                        try:
                            selection_id = int(input("Please enter a number for what you'd like to edit 1 (name) (2) priority or (3) description\n"))
                            match selection_id:
                                case 1:
                                    desired_name = input("Please enter the name for the ticket id (leave blank to not change anything) \n")
                                    
                                    if desired_name != "":
                                        df.loc[df['id'] == int(ticket_id), 'name'] = desired_name
                                    self.prompt_edit()
                                    break
                                case 2:
                                    while True:
                                        ticket_priority = input("Please enter a ticket priority (High, Medium, Low)\n")

                                        if ticket_priority.lower() == "high" or ticket_priority.lower() == "medium" or ticket_priority.lower() == "low":
                                            ticket_priority.capitalize()
                                            break
                                        else:
                                            print("Please enter a valid value")
                                    self.prompt_edit()
                                    break
                                case 3:
                                    description = input("Enter the description for the ticket (leave blank to not change anything)\n")
                                    if description != "":
                                        df.loc[df['id'] == int(ticket_id), 'description'] = description
                                    self.prompt_edit()
                                    break
                                case _:
                                    print("Please enter a valid selection.")
                        except ValueError:
                            print("You must enter a number!")
                else:
                    print("This ticket does not exist!")

                df.to_csv(file, index = False)
            elif ticket_id.lower() == "exit":
                self.edit_ticket = False
                break
            else:
                print("You did not enter a number!")
    
    def prompt_edit(self):
        still_editing = input("Would you like to continue editing?  y/n or yes/no\n")
        if still_editing.lower() == "n" or still_editing.lower() == "no":
            self.editing_ticket = False


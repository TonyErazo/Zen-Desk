from command.Command import Command

import os
import pandas as pd
import numpy as np
from pathlib import Path  
from command.impl.ViewCommand import ViewCommand

class DeleteCommand(Command):

    def __init__(self):
        Command.__init__(self, "/delete")
        self.view_command = ViewCommand()

    
    def execute(self):
        # Show curreent csv table
        self.view_command.execute()
        ticket_valid = False

        file_path = Path(__file__).parent / '..\..\data\\tickets\\'
        target_file = str(file_path) + "\\" + "datafile.csv"

        try:
            df = pd.read_csv(target_file, sep=",")

            while not ticket_valid:
                ticket_number = input("Please enter the ticket number only (Enter exit to leave this menu)\n")
            
                if ticket_number.isnumeric():
                    print("Accessing csv: " + target_file + "...")
                    selected = df[df['id'] == int(ticket_number)]

                    if not selected.empty:
                        selected_index = selected.index
                        print("selected index: " + str(selected_index))
                        df.drop(selected_index, inplace=True)
                        df.reset_index(drop=True)
                        df['id'] = np.arange(0, len(df))
                        print("Ticket has been deleted!")
                        ticket_valid = True
                        df.to_csv(target_file, index = False)
                    else:
                        print("Invalid ticket number!")
                # Exit delete section
                elif(ticket_number == "exit"):
                    ticket_valid = True
                else:
                    print("Please enter a number!")
        except FileNotFoundError as e:
            print("Ticket not found error! path: {} error: {}".format(target_file, e))
        except OSError as e:
            print("OSError! error: {}".format(e))





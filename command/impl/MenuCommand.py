from command.Command import Command

class MenuCommand(Command):

    def __init__(self):
        Command.__init__(self, "/menu")

    def execute(self):
        print("Welcome to the ZenDesk Menu")
        print("submit or /submit to submit/create a ticket")
        print("ls or /ls to display all the tickets")
        print("delete or /delete to delete a ticket")
        print("webapp or /webapp to launch the web application")
        print("exit or /exit to exit program")

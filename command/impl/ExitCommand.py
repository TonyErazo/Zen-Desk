from command.Command import Command

class ExitCommand(Command):

    def __init__(self):
        Command.__init__(self, "/exit")

    def execute(self):
        print("Closing program...")


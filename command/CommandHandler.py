from command.impl.ExitCommand import ExitCommand
from command.impl.MenuCommand import MenuCommand
from command.impl.SubmitCommand import SubmitCommand
from command.impl.ListCommand import ListCommand
from command.impl.DeleteCommand import DeleteCommand
from command.impl.ViewCommand import ViewCommand
from command.impl.EditCommand import EditCommand
from command.impl.WebAppCommand import WebAppCommand


class CommandHandler:

    def __init__(self):
        self.menu_command = MenuCommand()
        self.submit_command = SubmitCommand()
        self.exit_command = ExitCommand()
        self.list_command = ListCommand()
        self.delete_command = DeleteCommand()
        self.view_command = ViewCommand()
        self.edit_command = EditCommand()
        self.webapp_command = WebAppCommand()

    def process(self, terminal_input):
        match terminal_input:
            case "menu" | "/menu":
                self.menu_command.execute()
            case "submit" | "/submit":
                self.submit_command.execute()
            case "delete" | "/delete":
                self.delete_command.execute()
            case "ls" | "/ls":
                self.list_command.execute()
            case "view" | "/view":
                self.view_command.execute()
            case "edit" | "/edit":
                self.edit_command.execute()
            case "webapp" | "/webapp":
                self.webapp_command.execute()
            case "exit" | "/exit":
                self.exit_command.execute()
            case _:
                print("Please enter a valid command.")


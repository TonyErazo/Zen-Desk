from command.CommandHandler import CommandHandler
from command.impl.MenuCommand import MenuCommand

def main():
    print("Starting ZenDesk...")
    menu_command = MenuCommand()
    menu_command.execute()
    app_running = True
    command_handler = CommandHandler()
    while app_running:
        terminal_input = input("Please enter a command, to get started please type menu\n")

        if terminal_input == "exit" or terminal_input == "/exit":
            print("Closing...")
            app_running = False
        else:
            command_handler.process(terminal_input)


if __name__ == "__main__":
    main()

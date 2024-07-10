from abc import ABC

from src.commandfactory.Command import Command


class MenuCommand(Command):

    def __init__(self):
        Command.__init__(self, "/Menu")

    def execute(self):
        print("Welcome to the ZenDesk Menu")
        print("/submit to submit a ticket")
        print("/list to display all the tickets")

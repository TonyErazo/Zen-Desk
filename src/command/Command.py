from abc import ABC, abstractmethod


class Command(ABC):

    def __init__(self, command):
        self.command = command

    def get_command(self):
        return self.command

    @abstractmethod
    def execute(self):
        pass

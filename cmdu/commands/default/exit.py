
import argparse
from cmdu.commands.default.base import DefaultCommand


class ExitCommand(DefaultCommand):
    def __init__(self, shell):
        super().__init__(shell)
        self.name = "exit"
        self.parser = argparse.ArgumentParser(description="Exits the application")

    def run(self):
        print("Doing exit")
        self.shell.do_exit()

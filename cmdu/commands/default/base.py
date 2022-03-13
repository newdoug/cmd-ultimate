
from abc import ABC, abstractmethod
from typing import List
import argparse


class DefaultCommand(ABC):
    def __init__(self, shell):
        # TODO: these need to be set by child classes only
        self.name = ""
        self.parser = argparse.ArgumentParser(description="Default parser")
        self.parser.add_argument("--some-arg", "-a", help="optional arg")
        self.parsed_args = None
        self.category = "Built-in Commands"
        self.shell = shell


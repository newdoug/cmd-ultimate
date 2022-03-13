
from abc import ABC, abstractmethod
from typing import List
import argparse


class Command(ABC):
    def __init__(self, shell):
        # TODO: these need to be set by child classes only
        self.name = ""
        self.parser = argparse.ArgumentParser(description="Default parser")
        self.parser.add_argument("--some-arg", "-a", help="optional arg")
        self.parsed_args = None
        self.category = "No Category"
        self.shell = shell

    @abstractmethod
    def run(self):
        raise NotImplementedError()

    def run_raw_tokens(self, tokens: List[str]):
        self.parsed_args = self.parser.parse_args(tokens)
        self.run()

    def assign_to_category(self, category):
        self.category = category

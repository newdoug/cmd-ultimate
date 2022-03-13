
import argparse
from collections import defaultdict
from cmdu.commands.default.base import DefaultCommand


class HelpCommand(DefaultCommand):
    def __init__(self, shell):
        super().__init__(shell)
        self.name = "help"
        self.parser = argparse.ArgumentParser(description="Display available commands")
        self.parser.add_argument("--no-categories",
                                 help="Omit categorical organization")

    def run(self):
        print("Doing help")
        category_to_names = defaultdict(list)
        for command in self.shell.commands:
            category_to_names[command.category].append(command.name)
        for cat in category_to_names.keys():
            category_to_names[cat].sort()

        for cat, names in category_to_names.items():
            print(cat)
            # TODO: get terminal width, print to that width
            print("*"*20)
            print("\t".join(names))

        #out_str = "\t".join(command.name for command in self.shell.commands)
        #print(out_str)

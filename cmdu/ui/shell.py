import readline
import shlex
import sys
from typing import List

from cmdu.configuration.defaults import get_default_config
from cmdu.ui.exit_settings import ExitSettings
from cmdu.ui.prompt import Prompt
from cmdu.commands.default.exit import ExitCommand
from cmdu.commands.default.help import HelpCommand


class Shell:
    """
    The main shell of the application, handling interactions with the user
    """
    def __init__(self, config: dict = None):

        if not config:
            self.config = get_default_config()
        else:
            self.config = config
        # TODO: validate_config()
        
        self.commands = set()
        self.prompt = Prompt("CMDU> ")

        self._stay_alive = True
        self._exit_settings = ExitSettings()

        self.register_command(ExitCommand(self))
        self.register_command(HelpCommand(self))

    def register_command(self, command):
        self.commands.add(command)

    def display_prompt(self, continuation=False):
        if not continuation:
            out = self.prompt.ps1
        else:
            out = self.prompt.ps2
        print(out, end="", flush=True)
        #readline.redisplay()

    def _print_to_user(self, val, flush=True, end="\n"):
        # TODO: move to a separate class that handling this sort of thing? Like a printer class?
        # TODO: may need to handle logging to file, system logging, etc.
        print(val, flush=flush, end=end)

    def _get_user_input(self) -> List[str]:
        """Gets input from the user on the command line, returns tokens"""
        try:
            self.display_prompt()
            input_line = sys.stdin.readline()
            if not input_line:
                self._stay_alive = False
                self._print_to_user("CTRL-D: Exiting...")
                return []
            input_line = input_line.strip()
            while True:
                try:
                    split_line = shlex.split(input_line)
                    break
                except ValueError:
                    self._print_to_user(self.prompt.ps2, end="", flush=True)
                    input_line += sys.stdin.readline().strip()
            if not split_line:
                return []
            print("Got input: {}".format(input_line))
            print("Got tokens: ")
            for tok in split_line:
                print(tok)
            return split_line
        except KeyboardInterrupt:
            self._print_to_user("")
        return []

    def run_blank_user_input_action(self) -> bool:
        """Returns True on success, False on failure"""
        return True

    def process_token_input(self, tokens: List[str]) -> bool:
        if not tokens:
            return self.run_blank_user_input_action()
        command_string = tokens[0]
        print("Looks like command: {}".format(command_string))
        command_found = False
        for command in self.commands:
            if command.name == command_string:
                # TODO: return value? Could make use of it (bool (success), int (code), raise exception type?)
                command_found = True
                command.run()
                break
        if not command_found:
            self._print_to_user("Command not found: '{}'".format(command_string))
            #zreturn False

        return True

    def start(self):
        # Main running loop
        while self._stay_alive:
            tokens = self._get_user_input()
            if not self.process_token_input(tokens):
                break
        if not self.do_exit():
            return False
        return True

    def do_exit(self) -> bool:
        """Exits the application gracefully"""
        self._stay_alive = False
        return True

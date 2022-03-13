

from cmdu.configuration.defaults import get_default_prompt_config

_default_prompt_config = get_default_prompt_config()


class Prompt:
    def __init__(self, ps1: str, ps2: str = _default_prompt_config["PS2"]):
        self.ps1 = ps1
        self.ps2 = ps2

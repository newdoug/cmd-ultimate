import copy

from cmdu.configuration.kvs import (
    CONFIG_KEY_UI,
    CONFIG_KEY_PROMPT,
    CONFIG_KEY_HISTORY,
    UI_MODE_READLINE,
)

_default_config = {
    CONFIG_KEY_UI: {
        "mode": UI_MODE_READLINE,
    },
    CONFIG_KEY_PROMPT: {
        "PS1": "CMDU> ",
        "PS2": "> ",
    },
    CONFIG_KEY_HISTORY: {
        "write_cmd_history_on_exit": False,
        "write_stdout_history": False,
        "cmd_history_file": "cmd_history.txt",
        "stdout_history_file": "stdout_history.txt",
    },
}


def get_default_config() -> dict:
    return copy.deepcopy(_default_config)


def get_default_history_config() -> dict:
    return get_default_config()[CONFIG_KEY_HISTORY]


def get_default_ui_config() -> dict:
    return get_default_config()[CONFIG_KEY_UI]


def get_default_prompt_config() -> dict:
    return get_default_config()[CONFIG_KEY_PROMPT]

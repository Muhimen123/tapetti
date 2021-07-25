import sys
from typing import List, Dict, Union

from PyInquirer import prompt

from utils import command_controller


QUESTIONS: List[Dict[str, Union[str, List[str]]]] = [
    {
        "type": "list",
        "name": "command",
        "message": "Choose a command to apply",
        "choices": [
            "browse",
            "download",
            "help",
            "save",
            "search",
            "view"
        ]
    }
]

if len(sys.argv) < 2:
    sys.argv.append(prompt(QUESTIONS)["command"])

command_controller.command_controller(sys.argv)


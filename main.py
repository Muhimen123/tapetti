import sys

from PyInquirer import prompt

from utils import commandController

if len(sys.argv) < 2:
    questions = [
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

    sys.argv.append(prompt(questions)["command"])

commandController.command_controller(sys.argv)

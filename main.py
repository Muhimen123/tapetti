import sys
import os
from PyInquirer import prompt
from utils import commandController


arguments = sys.argv
if len(arguments) < 2:
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

    answer = prompt(questions)["command"]
    arguments.append(answer)

commandController.command_controller(arguments)

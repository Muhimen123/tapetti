import sys
import os
from utils import commandController


arguments = sys.argv
if len(arguments) < 2:
    print("Not enough arguments provided")
    # TODO: Replace this with help screen
else:
    commandController.command_controller(arguments)

import json
from rich import box
from rich.table import Table
from rich.console import Console


def help_message():
    with open('data/help_messages.json') as file:
        help_messages = json.load(file)

    table = Table(
        title="Available Commands",
        show_header=True,
        header_style="bold green",
        box=box.ROUNDED,
        show_lines=True
    )

    table.add_column("command")
    table.add_column("description")
    table.add_column("requirements")

    for command in help_messages:
        table.add_row(
            command["command_name"],
            command["description"],
            ", ".join(map(str, command["requirements"]))
        )

    console = Console()
    console.print(table)

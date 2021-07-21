import json
from typing import Dict, Union, List, Optional

from rich import box
from rich.table import Table
from rich.console import Console


def help_message() -> None:
    with open('data/help_messages.json') as file:
        help_messages: List[Dict[str, Union[str, List[Optional[str]]]]] = json.load(file)

    table: Table = Table(
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

    console: Console = Console()
    console.print(table)

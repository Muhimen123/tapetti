from typing import Dict, Union, List, Optional

from rich import box
from rich.table import Table
from rich.console import Console


def help_message() -> None:
    help_messages: List[Dict[str, Union[str, List[Optional[str]]]]] = [
      {
          "command_name": "browse",
          "description": "Browse image from the TID repo.",
          "requirements": [None]
      },
      {
          "command_name": "download",
          "description": "Downloads an image",
          "requirements": ["image link", "path", "file name"]
      },
      {
          "command_name": "help",
          "description": "Shows this message",
          "requirements": [None]
      },
      {
          "command_name": "save",
          "description": "Sets an image as the desktop wallpaper",
          "requirements": ["link or path"]
      },
      {
          "command_name": "search",
          "description": "Search images in the TID repo",
          "requirements": ["tag"]
      },
      {
          "command_name": "view",
          "description": "Open an image to preview",
          "requirements": ["image link or TID image number"] 
      }
    ]

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

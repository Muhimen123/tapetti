import requests
from rich import box
from rich.table import Table
from rich.console import Console
from colorama import Fore, Style


def browser_image(start: int = 0, limit: int = 15):
    """
    Browse all the wallpapers in the github repo
    and output a 'rich' table upon completion
    :param start: First index of the list
    :param limit: Number of wallpapers to show at once.
    """

    image_data_url = "https://raw.githubusercontent.com/Muhimen123/TID/main/image_data.json"

    try:
        response = requests.get(image_data_url)
        if response.ok:
            generate_table(response.json())
        else:
            print(Fore.RED + f"Oops, something went wrong {response.status_code}" + Style.RESET_ALL)

    except Exception as error:
        print(Fore.RED + "Turns out you are not connected to the internet" + Style.RESET_ALL)


def generate_table(image_data: list):
    """
    Create and print a python rich table
    :param image_data: list of dicts containing information about images
    """

    image_data_table = Table(
        show_header=True,
        header_style="bold green",
        box=box.ROUNDED,
        show_lines=True
    )

    image_data_table.add_column("No.")
    image_data_table.add_column("Name")
    image_data_table.add_column("File Type")
    image_data_table.add_column("Resolution")
    image_data_table.add_column("Orientation")
    image_data_table.add_column("Theme")
    image_data_table.add_column("Color")

    for idx, image in enumerate(image_data):
        height = image["height"]
        width = image["width"]

        image_data_table.add_row(
            str(idx + 1),
            image["image_name"],
            image["file_type"],
            f"{width}x{height}",
            "Horizontal" if width > height else "Vertical",
            image["theme"],
            " ".join(image["color"][:min(len(image["color"]), 3)])
        )

    console = Console()
    console.print(image_data_table)

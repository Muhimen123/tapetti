import os
import ctypes
import platform
from pathlib import Path
from typing import List, Union, Dict, Optional, AnyStr, Any

from utils import downloader
from PyInquirer import prompt
from colorama import Fore, Style
from utils.image_viewer import tid_repo_prompt


def save_image() -> None:
    """
    sets the image as the desktop wallpaper
    If a link is given then first download the image
    """

    questions: List[Dict[str, Union[List[str], str]]] = [
        {
            "type": "list",
            "name": "download_type",
            "message": "Set wallpaper from: ",
            "choices": [
                "TID Repo",
                "Link",
                "Path"
            ]
        }
    ]

    answer: Dict = prompt(questions)["download_type"]

    if answer != 'Path':
        link: Optional[str] = tid_repo_prompt(
            "https://raw.githubusercontent.com/Muhimen123/TID/main/image_data.json"
        ) if answer == 'TID Repo' else input("Please enter download link: ")

        path: str = "//" + os.path.join(os.getcwd(), "data", "images")
        downloader.download_image(link, path, "current_desktop_wallpaper.png")
        wallpaper_path: str = f"{path}current_desktop_wallpaper.png"

    else:
        questions: List[Dict[str, Union[List[str], str]]] = [
            {
                "type": "list",
                "name": "path_type",
                "message": "Choose path type: ",
                "choices": [
                    "Default Path",
                    "Relative Path",
                    "Absolute Path"
                ]
            }
        ]

        answer: Dict = prompt(questions)['path_type']

        if answer == "Default Path":
            path: str = os.path.join(os.getcwd(), "data", "images")

        elif answer == "Relative Path":
            path: str = os.path.join(
                os.getcwd(),
                input("Relative path(dont' include the file name): ")
            )

        else:
            path: str = input("Absolute path(don't include the file name): ")

        while True:
            wallpaper_path: str = os.path.join(
                path, input("File name(include the extension): ")
            )

            if os.path.isfile(wallpaper_path):
                break

            print(Fore.RED + f"No file found in path {path}" + Fore.BLUE)

    system_os: str = platform.system()

    if system_os == "Windows":
        is_changed: bool = change_windows_wallpaper(wallpaper_path)

    elif system_os == "Darwin":
        is_changed: bool = change_mac_wallpaper(wallpaper_path)

    elif system_os == "Linux":
        is_changed: bool = change_linux_wallpaper(wallpaper_path)

    else:
        print(Fore.RED + "Sorry, couldn't detect OS.")
        is_changed: bool = False

    print(
        (
            f"{Fore.GREEN}Changed the wallpaper"
            if is_changed else
            f"{Fore.RED}Couldn't change the wallpaper"
        ),
        Style.RESET_ALL
    )


def change_windows_wallpaper(wallpaper_path: str) -> bool:
    is_changed: bool = ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)

    # Windows resets back to old wallpaper everytime pc reboots.
    # This portion of code aims to solve it by changing the main
    # wallpaper from the root path. 

    with open(wallpaper_path, "rb") as file:
        wallpaper_image: AnyStr = file.read()

        suffix_path: str = "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper"
        windows_wallpaper_path: str = f"{Path.home()}{suffix_path}"

        if os.path.isfile(windows_wallpaper_path):
            with open(windows_wallpaper_path, "wb") as img_file:
                img_file.write(wallpaper_image)

        else:
            print("Changed wallpaper temporarily. Might get changed when pc reboots")
            # TODO: Create a fix for this

    return is_changed


def change_mac_wallpaper(wallpaper_path: str) -> bool:
    print("Oops, MacOS not yet supported")
    return False


def change_linux_wallpaper(wallpaper_path: str) -> bool:
    de: Any = os.environ.get("XDG_CURRENT_DESKTOP")

    if de and "gnome" in de:
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{wallpaper_path}")
        return True

    print(f"Did not recognise DE, defaulting to using `feh` to set wallpaper")
    os.system(f"feh --bg-scale {wallpaper_path}")
    return True

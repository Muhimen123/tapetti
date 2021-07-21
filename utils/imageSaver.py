import os
import ctypes
import platform
from pathlib import Path
from utils import downloader
from PyInquirer import prompt
from colorama import Fore, Style
from utils.imageViewer import tid_repo_prompt


def save_image():
    """
    sets the image as the desktop wallpaper
    If a link is given then first download the image
    :param path: Absolute or relative path to the file
    """

    questions = [
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

    answer = prompt(questions)["download_type"]

    if answer != 'Path':
        if answer == 'TID Repo':
            image_data_url = "https://raw.githubusercontent.com/Muhimen123/TID/main/image_data.json"
            link = tid_repo_prompt(image_data_url)

        else:
            link = input("Please enter download link: ")

        path = os.path.join(os.getcwd(), "data", "images")
        downloader.download_image(link, path, "current_desktop_wallpaper.png")
        wallpaper_path = path + "current_desktop_wallpaper.png"

    else:
        questions = [
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

        answer = prompt(questions)['path_type']

        if answer == "Default Path":
            path = os.path.join(os.getcwd(), "data", "images")

        elif answer == "Relative Path":
            path = os.path.join(
                os.getcwd(),
                input("Relative path(dont' include the file name): ")
            )

        else:
            path = input("Absolute path(don't include the file name): ")

        while True:
            wallpaper_path = os.path.join(
                path,
                input("File name(include the extension): ")
            )

            if os.path.isfile(wallpaper_path):
                break

            print(Fore.RED + f"No file found in path {path}" + Fore.BLUE)

    system_os = platform.system()

    if system_os == "Windows":
        is_changed = change_windows_wallpaper(wallpaper_path)

    elif system_os == "Darwin":
        is_changed = change_mac_wallpaper(wallpaper_path)

    elif system_os == "Linux":
        is_changed = change_linux_wallpaper(wallpaper_path)

    else:
        print(Fore.RED + "Sorry, couldn't detect OS.")
        is_changed = 0

    if is_changed:
        print(Fore.GREEN + "Changed the wallpaper")

    else:
        print(Fore.RED + "Couldn't change the wallpaper")

    print(Style.RESET_ALL)


def change_windows_wallpaper(wallpaper_path):
    is_changed = ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)

    # Windows resets back to old wallpaper everytime pc reboots.
    # This portion of code aims to solve it by changing the main
    # wallpaper from the root path. 

    with open(wallpaper_path, "rb") as file:
        wallpaper_image = file.read()

        windows_wallpaper_path = f"{Path.home()}\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper"
        if os.path.isfile(windows_wallpaper_path):
            with open(windows_wallpaper_path, "wb") as img_file:
                img_file.write(wallpaper_image)
        else:
            print("Changed wallpaper temporarily. Might get changed when pc reboots")
            # TODO: Create a fix for this

    return is_changed


def change_mac_wallpaper(wallpaper_path):
    print("Oops, MacOS not yet supported")
    return False


def get_linux_desktop_environment():
    return os.environ.get("XDG_CURRENT_DESKTOP")


def change_linux_wallpaper(wallpaper_path):
    de = get_linux_desktop_environment()

    if de and "gnome" in de:
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{wallpaper_path}")
        return True

    print(f"Did not recognise DE, defaulting to using `feh` to set wallpaper")
    os.system(f"feh --bg-scale {wallpaper_path}")
    return True
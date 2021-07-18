import os
import ctypes
import platform
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

        path = os.getcwd() + "\\data\\images\\"
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
            path = os.getcwd() + "\\data\\images\\"
        elif answer == "Relative Path":
            path = input("Relative path(dont' include the file name): ")
            path = os.getcwd() + "\\" + path + "\\"
        else:
            path = input("Absolute path(don't include the file name): ") + "\\"

        while True:
            file_name = input("File name(include the extension): ")
            wallpaper_path = path + file_name

            if os.path.isfile(wallpaper_path):
                break
            else:
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
    is_changed = ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
    return is_changed

def change_mac_wallpaper(wallpaper_path):
    print("Oops, MacOS not yet supported")
    return 0


def change_linux_wallpaper(wallpaper_path):
    print("Oops, GNU/Linux not yet supported")
    return 0


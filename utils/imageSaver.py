import os
import ctypes
from utils import downloader
from PyInquirer import prompt
from colorama import Fore, Style


def save_image():
    """
    sets the image as the desktop wallpaper
    If a link is given then first download the image
    :param path: Absolute or relative path to the file
    """

    print(Fore.BLUE, end="") 
    
    questions = [
        {
            "type": "list",
            "name": "download_type",
            "message": "Set wallpaper from: ",
            "choices": [
                "Link",
                "Path"
            ]
        }
    ]

    answer = prompt(questions)["download_type"]

    if answer == 'Link':
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


    is_changed = ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

    if is_changed:
        print(Fore.GREEN + "Changed the wallpaper")
    else:
        print(Fore.RED + "Couldn't change the wallpaper")

    print(Style.RESET_ALL)


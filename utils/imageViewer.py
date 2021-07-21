import os
import requests
from PIL import Image
from utils import downloader
from PyInquirer import prompt
from colorama import Fore, Style


def image_viewer():

    """
    preview an image
    """

    # If the link is not provided then take input from the user
    image_data_url = "https://raw.githubusercontent.com/Muhimen123/TID/main/image_data.json"
    questions = [
        {
            "type": "list",
            "name": "view_type",
            "message": "View image from: ",
            "choices": [
                "TID Repo",
                "Image Link"
            ]
        }
    ]
    
    answer = prompt(questions)["view_type"]

    if answer == "TID Repo":
        link = tid_repo_prompt(image_data_url)
        if link is None:
            return -1

    else:
        link = input("Please enter download link: ")

    path = f"{os.getcwd()}\\data\\images\\"

    downloader.download_image(link, path, "tmp_wallpaper_preview_image.png")
    Image.open(path + "tmp_wallpaper_preview_image.png").show()


def tid_repo_prompt(image_data_url: str):

    """
    Prompt for TID repo image selection
    :param image_data_url: base url of the TID repo imaegs
    :return: download link of the image or None
    """

    entry_number = int(input("Please enter image number: ")) - 1

    try:
        response = requests.get(image_data_url)

        if not response.ok:
            print(Fore.RED + f"Oops, something went wrong {response.status_code}" + Style.RESEST_ALL)
            return

        image_data = response.json()
        if entry_number >= len(image_data):
            entry_number = 1

        file_name = image_data[entry_number]["image_name"]
        file_type = image_data[entry_number]["file_type"]
        return f"https://raw.githubusercontent.com/Muhimen123/TID/main/images/{file_name}.{file_type}"

    except Exception as error:
        print(error)
        print(Fore.RED + "Perhaps you are not connected to the internet. Mind checking it again?" + Style.RESEST_ALL)
    
    return link

import os
import requests
from PyInquirer import prompt
from colorama import Fore, Back, Style


def download_image(link: str = None, path: str = None, file_name: str = None):

    """
    Download the given image in the given path
    :param link: Link to download the image
    :param file_name: What name to give the file while saving
    :param path: Where to save the file. Can be either absolute or relative
    """

    if link is None:
        link, path, file_name = download_prompt()

    try:
        print("Downloading the file")
        response = requests.get(link)

        if response.status_code == 200:
            with open(path+file_name, "wb") as file:
                file.write(response.content)
            print(Fore.GREEN + "Downloaded successfully" + Style.RESET_ALL)

        else:
            print(response.status_code, "Error")

    except Exception as error:
        print(error)
        pass
        # TODO: Show proper error message


def download_prompt():

    """
    Show a prompt to gather necessary data
    :return: link, path, file_name
    """
    questions = [
        {
            "type": "list",
            "name": "path_type",
            "message": "Choose path type: ",
            "choices": [
                "Default Path",
                "Absolute Path",
                "Relative Path"
            ]
        }
    ]

    print(Fore.BLUE, end="")

    link = input("Please enter download link: ")

    answer = prompt(questions)['path_type']

    if answer == "Default Path":
        path = os.getcwd() + "\\data\\images\\"
    elif answer == "Relative Path":
        path = input("Download path: ")
        path = os.getcwd() + "\\" + path + "\\"
    else:
        path = input("Download path: ") + "\\"

    while True:
        file_name = input("File name(include extension): ")

        if os.path.isfile(path + '\\' + file_name):
            print(Fore.RED + "A file with the name already exists. Please enter another one." + Fore.GREEN)
        else:
            break

    print(Style.RESET_ALL, end="")

    return link, path, file_name


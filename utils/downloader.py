import os
import requests
from PyInquirer import prompt
from rich.progress import Progress
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
        download_content(link, path, file_name)

    except Exception as error:
        print(error)
        pass
        # TODO: Show proper error message


def download_content(link: str, path: str, file_name: str):
    """
    Downloads the image with request stream and shows downloading progress bar
    :param link: link of the image to download
    :param path: path where to download the image
    :param file_name: Name for the downloaded image
    """

    with requests.get(link, stream=True) as res:
        image_size = int(res.headers.get('content-length', 0))
        chunk_size = 1024
        image_content = res.iter_content(chunk_size)

        with Progress() as progress:
            download_task = progress.add_task(f"[green] {file_name}", total=image_size)

            full_path = path + file_name
            with open(full_path, "wb") as image_file:
                for chunk in image_content:
                    image_file.write(chunk)
                    progress.update(download_task, advance=len(chunk))

            while not progress.finished:
                progress.update(task, advance=chunk_size)


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
            print(Fore.RED + "A file with the name already exists. Please enter another one." + Style.RESET_ALL)
        else:
            break

    return link, path, file_name


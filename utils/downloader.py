import os
from typing import Optional, Iterator, List, Dict, Union, Tuple

import requests
from PyInquirer import prompt
from rich.progress import Progress, TaskID
from colorama import Fore, Back, Style


def download_image(
        link: Optional[str] = None,
        path: Optional[str] = None,
        file_name: Optional[str] = None
) -> None:
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
        # TODO: Show proper error message


def download_content(link: str, path: str, file_name: str) -> None:
    """
    Downloads the image with request stream and shows downloading progress bar
    :param link: link of the image to download
    :param path: path where to download the image
    :param file_name: Name for the downloaded image
    """

    with requests.get(link, stream=True) as res:
        image_size: int = int(res.headers.get('content-length', 0))
        chunk_size: int = 1024
        image_content: Iterator = res.iter_content(chunk_size)

    with Progress() as progress:
        download_task: TaskID = progress.add_task(f"[green] {file_name}", total=image_size)

        with open(path + file_name, "wb") as image_file:
            for chunk in image_content:
                image_file.write(chunk)
                progress.update(download_task, advance=len(chunk))

        while not progress.finished:
            progress.update(task, advance=chunk_size)


def download_prompt() -> Tuple[str, str, str]:
    """
    Show a prompt to gather necessary data
    :return: link, path, file_name
    """
    questions: List[Dict[str, Union[str, List[str]]]] = [
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

    link: str = input("Please enter download link: ")
    answer: Dict = prompt(questions)['path_type']

    if answer == "Default Path":
        path: str = f"{os.getcwd()}\\data\\images\\"

    elif answer == "Relative Path":
        path: str = input("Download path: ")
        path: str = f"{os.getcwd()}\\{path}\\"

    else:
        path: str = input("Download path: ") + "\\"

    while True:
        file_name: str = input("File name(include extension): ")

        if not os.path.isfile(f"{path}\\{file_name}"):
            break

        print(Fore.RED + "A file with the name already exists. Please enter another one." + Style.RESET_ALL)

    return link, path, file_name

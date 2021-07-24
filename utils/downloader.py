import os
from typing import Optional, Iterator, List, Dict, Union, Tuple

import requests
from PyInquirer import prompt
from colorama import Fore, Style
from rich.progress import Progress, TaskID


QUESTIONS: List[Dict[str, Union[str, List[str]]]] = [
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

    if not os.path.exists(path):
        os.mkdir(path)

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
        download_with_progress(res, path, file_name)


def download_with_progress(res, path: str, file_name: str) -> None:
    image_size: int = int(res.headers.get('content-length', 0))
    chunk_size: int = 1024
    image_content: Iterator = res.iter_content(chunk_size)

    file_path: str = os.path.join(path, file_name)

    with Progress() as progress:
        download_task: TaskID = progress.add_task(f"[green] {file_name}", total=image_size)

        save_image_content(file_path, image_content, progress, download_task)

        while not progress.finished:
            progress.update(download_task, advance=chunk_size)


def save_image_content(
        file_path: str,
        image_content: Iterator,
        progress: Progress,
        download_task: TaskID
) -> None:
    with open(file_path, "wb") as image_file:
        for chunk in image_content:
            image_file.write(chunk)

            progress.update(download_task, advance=len(chunk))


def download_prompt() -> Tuple[str, str, str]:
    """
    Show a prompt to gather necessary data
    :return: link, path, file_name
    """
    link: str = input("Please enter download link: ")
    answer: Dict = prompt(QUESTIONS)['path_type']

    if answer == "Default Path":
        path: str = os.path.join(os.getcwd(), "data", "images")

    elif answer == "Relative Path":
        path: str = input("Download path: ")
        path: str = os.path.join(os.getcwd(), path)

    else:
        path: str = input("Download path: ") + os.path.pathsep

    return link, path, get_new_file_name(path)


def get_new_file_name(path: str) -> str:
    """Ensure the user enter a new file_name."""
    text: str = "File name(include extension): "
    file_name: str = input(text)

    while not file_name or os.path.isfile(os.path.join(path, file_name)):
        print(
            Fore.RED +
            "A file with the name already exists or the filename is invalid. Please enter another one."
            + Style.RESET_ALL
        )

        file_name: str = input(text)

    return file_name

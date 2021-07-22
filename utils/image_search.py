from typing import List

import requests
from colorama import Fore

from utils.image_browser import generate_table


def search_image() -> None:
    """
    Search for images that contains the given tag
    and output a 'rich' table upon completion
    """

    image_data_url: str = "https://raw.githubusercontent.com/Muhimen123/TID/main/image_data.json"
    tag: str = input("Please enter a tag: ")

    try:
        response: requests.Response = requests.get(image_data_url)

        if response.ok:
            filtered_result: List = filter_result_by_tag(response.json(), tag)
            generate_table(filtered_result)

        else:
            print(Fore.RED + "Oops, something went wrong. {response.status_code}")

    except Exception as error:
        print(error)
        print(Fore.RED + "Perhaps you are not connected to the internet.")


def filter_result_by_tag(image_data: list, tag: str) -> List:
    """
    filters the search result by the given tag
    :param image_data: list of dict. the raw data from TID repo
    :param tag: the tag to apply filter
    :return: list of dict. filtered dict 
    """
    return [image for image in image_data if tag in image["tags"]]

from typing import List

import requests
from rich import print as rprint
from PyInquirer import prompt

from utils.image_browser import generate_table


def search_image() -> None:
    """
    Search for images that contains the given tag
    and output a 'rich' table upon completion
    """

    image_data_url: str = "https://raw.githubusercontent.com/Muhimen123/TID/main/image_data.json"

    filters = Filter()
    actions = {
        "tag": filters.filter_result_by_tag,
    }

    #TODO: Add chain filter (multiple filter at once)
    questions = [
        {
            "type": "list",
            "name": "fliter",
            "message": "Select a filter method",
            "choices": [
                "Tag"
            ]
        }
    ]

    answer: str = prompt(questions)["fliter"]

    try:
        response: requests.Response = requests.get(image_data_url)

        if response.ok:
            filtered_result: List = actions[answer.lower()](response.json())
            generate_table(filtered_result)

        else:
            rprint("[red]Oops, something went wrong. {response.status_code}")

    except requests.exceptions.RequestException:
        rprint("[red]Perhaps you are not connected to the internet.")


class Filter:

    @staticmethod
    def filter_result_by_tag(image_data: list )-> List:
        """
        filters the search result by the given tag
        :param image_data: list of dict. the raw data from TID repo
        :return: list of dict. filtered dict
        """
        tag = input("Enter tag name: ")
        return [image for image in image_data if tag.lower() in [img_tag.lower() for img_tag in image["tags"]]]

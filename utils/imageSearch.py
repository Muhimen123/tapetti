import requests
from rich import box
from rich.table import Table
from rich.console import Console
from colorama import Fore, Style 

from utils.imageBrowser import generate_table

def search_image():
    """
    Search for images that contains the given tag
    and output a 'rich' table upon completion
    """
    
    image_data_url = "https://raw.githubusercontent.com/Muhimen123/TID/main/image_data.json"
    tag = input("Please enter a tag: ")

    try:
        response = requests.get(image_data_url)
        if response.status_code == 200:
            filtered_result = filter_result_by_tag(response.json(), tag)
            generate_table(filtered_result)
        else:
            print(Fore.RED + "Oops, something went wrong. {response.status_code}")
    except Exception as error:
        print(error)
        print(Fore.RED + "Perhaps you are not connected to the internet.")


def filter_result_by_tag(image_data: list, tag: str) -> list: 
    """
    filters the search result by the given tag
    :param image_data: list of dict. the raw data from TID repo
    :param tag: the tag to apply filter
    :return: list of dict. filtered dict 
    """

    filtered_result = [] 

    for image in image_data:
        tags = image["tags"]
        if tag in tags:
            filtered_result.append(image)

    return filtered_result


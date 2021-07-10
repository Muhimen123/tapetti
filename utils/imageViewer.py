from PIL import Image
import os

from utils import downloader


def image_viewer(link: str = None):

    """
    Show an image without downloading it
    :param link: link to the image
    """

    # If the link is not provided then take input from the user
    if link is None:
        link = input("Please enter the image link: ")

    path = os.getcwd() + "\\data\\images\\"
    downloader.download_image(link, path, "tmp_wallpaper_preview_image.png")

    img = Image.open(path + "tmp_wallpaper_preview_image.png")
    img.show()


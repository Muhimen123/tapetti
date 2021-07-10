from utils import imageViewer
from utils import downloader
from utils import imageSaver


def command_controller(command: list):
    """
    Route to the correct command and fire the function
    :param command:
    """

    if "view".upper() in command[1].upper():
        if len(command) >= 3:
            link = command[2]
            imageViewer.image_viewer(link)
        else:
            imageViewer.image_viewer()

    elif "download".upper() in command[1].upper():
        downloader.download_image()

    elif "save".upper() in command[1].upper():
        imageSaver.save_image()

from utils import imageViewer
from utils import downloader
from utils import imageSaver
from utils import imageBrowser
from utils import imageSearch
from utils import helpMessage

actions = {
    "view": imageViewer.image_viewer,
    "download": downloader.download_image,
    "save": imageSaver.save_image,
    "browse": imageBrowser.browser_image,
    "search": imageSearch.search_image,
    "help": helpMessage.help_message
}


def command_controller(command: list):
    """
    Route to the correct command and fire the function
    :param command:
    """
    action = actions.get(command[1].lower())

    if not callable(action):
        return

    action()

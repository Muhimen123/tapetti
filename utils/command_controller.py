from typing import Dict, Callable, Any, List

from utils import downloader
from utils import help_message
from utils import image_browser
from utils import image_saver
from utils import image_search
from utils import image_viewer



Action = Callable[[], Any]

actions: Dict[str, Action] = {
    "view": image_viewer.image_viewer,
    "download": downloader.download_image,
    "save": image_saver.save_image,
    "browse": image_browser.browser_image,
    "search": image_search.search_image,
    "help": help_message.help_message
}


def command_controller(command: List[str]) -> None:
    """
    Route to the correct command and fire the function
    :param command:
    """
    action: Action = actions.get(command[1].lower())

    if not callable(action):
        return

    action()


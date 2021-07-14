from utils import imageViewer
from utils import downloader
from utils import imageSaver
from utils import imageBrowser
from utils import imageSearch  
from utils import helpMessage 

def command_controller(command: list):
    """
    Route to the correct command and fire the function
    :param command:
    """

    if "view".upper() in command[1].upper():
        imageViewer.image_viewer()

    elif "download".upper() in command[1].upper():
        downloader.download_image()

    elif "save".upper() in command[1].upper():
        imageSaver.save_image()

    elif "browse".upper() in command[1].upper():
        imageBrowser.browser_image()
    
    elif "search".upper() in command[1].upper():
        imageSearch.search_image()

    elif "help".upper() in command[1].upper():
        helpMessage.help_message()


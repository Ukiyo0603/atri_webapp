from .atri import Atri
from fastapi import Request, Response
from atri_utils import *
import urllib.parse

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    # query = {
    #     "Home": "Home",
    #     "About": "About",
    #     "Menu": "Menu",
    #     "Pages": "Pages",
    #     "Cart": "Cart"
    # }

    # url = "/pagename" + "?" + urllib.parse.urlencode(query)
    # res.headers.append("location", url)
    

    if at.Button19.onClick:
        at.Flex157.styles.display = 'flex'
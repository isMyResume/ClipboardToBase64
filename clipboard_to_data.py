import os

import win32clipboard
from PIL import ImageGrab

from utility import generate_filepath


def get_image_clipboard():
    clipboard_data = ImageGrab.grabclipboard()
    return clipboard_data


def clipboard_image_to_png(clipboard_data):
    filepath = generate_filepath('png', os.getcwd() + '/image/')
    clipboard_data.save(filepath)
    return filepath


def get_text_clipboard():
    win32clipboard.OpenClipboard()
    clipboard_data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return clipboard_data

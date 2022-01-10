import os

from PIL import ImageGrab

from utility import generate_filepath


def get_clipboard():
    clipboard_image = ImageGrab.grabclipboard()
    return clipboard_image


def clipboard_image_to_png(clipboard_image):
    filepath = generate_filepath('png', os.getcwd() + '/image/')
    clipboard_image.save(filepath)
    return filepath

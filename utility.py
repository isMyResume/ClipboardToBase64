from io import BytesIO

import win32clipboard
from PIL import ImageGrab, ImageFile, Image


def get_clipboard():
    clipboard_image = ImageGrab.grabclipboard()
    return clipboard_image


def set_clipboard_image(filepath):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def set_empty_clipboard():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()

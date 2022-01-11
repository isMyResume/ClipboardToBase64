import datetime
import uuid
from io import BytesIO
from pathlib import Path

import PIL
import win32clipboard
import win32con
from PIL import ImageFile, Image


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


def createDirectory(path):
    path = Path.cwd() / path
    path.mkdir(parents=True, exist_ok=True)
    directoryPath = str(path) + "\\"
    return directoryPath


def generate_filepath(ext, path=''):
    createDirectory(path)
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filepath = path + now + '_' + str(uuid.uuid4()) + '.' + ext
    return filepath


def get_image_file(path):
    with PIL.Image.open(path) as image:
        return image


def set_clipboard_text(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()
    return text

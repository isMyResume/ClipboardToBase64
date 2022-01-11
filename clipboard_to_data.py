import win32clipboard
from PIL import ImageGrab
from matplotlib.sphinxext.mathmpl import latex2png

from utility import generate_filepath


def get_image_clipboard():
    clipboard_data = ImageGrab.grabclipboard()
    return clipboard_data


def clipboard_image_to_png(clipboard_data):
    filepath = generate_filepath('png', 'image/')
    clipboard_data.save(filepath)
    return filepath


def get_text_clipboard():
    win32clipboard.OpenClipboard()
    clipboard_data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return clipboard_data


def is_tex(clipboard_data):
    if clipboard_data.startswith("$") and clipboard_data.endswith("$"):
        str_type = 'tex'
    else:
        str_type = 'plaintext'
    return str_type


def tex_to_png(equations):
    latex = equations[1:-1]
    filepath = generate_filepath('png', 'image/')

    latex2png(latex, filepath, fontsize=10, dpi=600)
    return filepath

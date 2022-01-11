import PIL

from clipboard_to_data import get_image_clipboard, clipboard_image_to_png, get_text_clipboard, is_tex, tex_to_png
from data_to_base64 import pngimagefile_to_base64, convert_markdown_image_tag
from tag_to_clipboard import set_image_tag_clipboard


def get_clipboard():
    try:
        clipboard_data = get_text_clipboard()
    except TypeError:
        clipboard_data = get_image_clipboard()
    return clipboard_data


def clipboard_image_to_base64_tag(clipboard_data):
    filepath = clipboard_image_to_png(clipboard_data)
    base64_encoded = pngimagefile_to_base64(filepath)
    image_tag = convert_markdown_image_tag(filepath, base64_encoded)
    image_tag = set_image_tag_clipboard(image_tag)
    return image_tag

def clipboard_tex_image_to_base64_tag(clipboard_data,equation):
    base64_encoded = pngimagefile_to_base64(clipboard_data)
    image_tag = convert_markdown_image_tag(equation, base64_encoded)
    image_tag = set_image_tag_clipboard(image_tag)
    return image_tag


def get_clipboard_to_base64():
    clipboard_data = get_clipboard()
    if isinstance(clipboard_data, str):
        clipboard_data = clipboard_data
        if is_tex(clipboard_data) == 'tex':
            equation = clipboard_data
            clipboard_data = tex_to_png(clipboard_data)
            clipboard_data = clipboard_tex_image_to_base64_tag(clipboard_data,equation)
    elif isinstance(clipboard_data, PIL.PngImagePlugin.PngImageFile):
        clipboard_data = clipboard_image_to_base64_tag(clipboard_data)
    return clipboard_data

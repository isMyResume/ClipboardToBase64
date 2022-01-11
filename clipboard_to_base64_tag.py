from clipboard_to_data import get_image_clipboard, clipboard_image_to_png
from data_to_base64 import pngimagefile_to_base64, convert_markdown_image_tag
from tag_to_clipboard import set_image_tag_clipboard


def clipboard_image_to_base64_tag():
    clipboard_data = get_image_clipboard()
    filepath = clipboard_image_to_png(clipboard_data)
    base64_encoded = pngimagefile_to_base64(filepath)
    image_tag = convert_markdown_image_tag(filepath, base64_encoded)
    set_image_tag_clipboard(image_tag)
    return filepath

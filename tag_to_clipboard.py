import win32clipboard
import win32con


def set_image_tag_clipboard(image_tag):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, image_tag)
    win32clipboard.CloseClipboard()
    return image_tag
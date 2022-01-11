import os
import re
from unittest import TestCase

import PIL

from clipboard_to_base64_tag import clipboard_image_to_base64_tag, get_clipboard
from clipboard_to_data import get_text_clipboard, clipboard_image_to_png
from utility import set_clipboard_image, set_empty_clipboard, set_clipboard_text, get_image_file

test_image_file = 'animal.png'
test_markdown_tag_file = 'markdown_animal_png.txt'


class TestClipboardToBase64Tag(TestCase):
    def setUp(self) -> None:
        set_clipboard_image(test_image_file)
        with open(test_markdown_tag_file, 'r') as text:
            base64_text = text.read()
        re_alt = "\(.*\)|\s-\s.*"
        self.alt_tag = re.sub(re_alt, '', base64_text)
        self.alt_tag = self.alt_tag.replace('![', '').replace(']', '')
        self.data_tag = base64_text.replace(self.alt_tag, '')

    def test_clipboard_to_base64_tag(self):
        image_tag = clipboard_image_to_base64_tag(get_clipboard())
        re_alt = "\(.*\)|\s-\s.*"
        self.alt_tag_path = re.sub(re_alt, '', image_tag)
        self.alt_tag_path = self.alt_tag_path.replace('![', '').replace(']', '')
        data_tag = get_text_clipboard().replace(self.alt_tag_path, '')

        self.assertEqual('animal.png', self.alt_tag)
        self.assertEqual(data_tag, self.data_tag)

    def tearDown(self) -> None:
        set_empty_clipboard()
        os.remove('image/' + self.alt_tag_path)


class TestGetClipboardTypeStr(TestCase):
    def setUp(self) -> None:
        set_clipboard_text('text')

    def test_get_clipboard(self):
        clipboard_data = get_clipboard()
        self.assertIsInstance(clipboard_data, str)

    def tearDown(self) -> None:
        set_empty_clipboard()


class TestGetClipboardTypeImage(TestCase):
    def setUp(self) -> None:
        set_clipboard_image(test_image_file)

    def test_get_clipboard(self):
        self.filepath = clipboard_image_to_png(get_clipboard())
        clipboard_data = get_image_file(self.filepath)
        self.assertEqual(type(clipboard_data), PIL.PngImagePlugin.PngImageFile)

    def tearDown(self) -> None:
        set_empty_clipboard()
        os.remove(self.filepath)

import os
import re
from unittest import TestCase

from clipboard_to_base64_tag import clipboard_image_to_base64_tag
from clipboard_to_data import get_text_clipboard
from utility import set_clipboard_image

test_image_file = 'animal.png'
test_markdown_tag_file = 'markdown_animal_png.txt'


class TestClipboardToBase64Tag(TestCase):
    def setUp(self) -> None:
        set_clipboard_image(test_image_file)
        with open(test_markdown_tag_file, 'r') as text:
            base64_text = text.read()
        re_alt = "\(.*\)|\s-\s.*"
        self.alt_tag = re.sub(re_alt, '', base64_text)
        self.data_tag = base64_text.replace(self.alt_tag, '')

    def test_clipboard_to_base64_tag(self):
        self.filepath = clipboard_image_to_base64_tag()
        re_alt = "\(.*\)|\s-\s.*"
        alt_tag = re.sub(re_alt, '', get_text_clipboard())
        data_tag = get_text_clipboard().replace(alt_tag, '')
        self.assertEqual('![animal.png]', self.alt_tag)
        self.assertEqual(data_tag, self.data_tag)

    def tearDown(self) -> None:
        os.remove(self.filepath)

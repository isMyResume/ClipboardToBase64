from unittest import TestCase

from tag_to_clipboard import set_image_tag_clipboard
from clipboard_to_data import get_text_clipboard

test_markdown_tag_file = 'markdown_animal.txt'


class TestTagToClipboard(TestCase):
    def setUp(self) -> None:
        with open(test_markdown_tag_file, 'r') as text:
            self.base64_text = text.read()

    def test_imagetag_to_clipboard(self):
        set_image_tag_clipboard(self.base64_text)
        self.assertEqual(get_text_clipboard(), self.base64_text)

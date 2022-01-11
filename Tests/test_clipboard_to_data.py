import os
import unittest
from unittest import TestCase

import PIL

from clipboard_to_data import clipboard_image_to_png, get_image_clipboard
from utility import set_clipboard_image, set_empty_clipboard, get_image_file

test_image_file = 'animal.png'


class TestGetClipboard(TestCase):
    def setUp(self) -> None:
        set_clipboard_image(test_image_file)

    def test_get_clipboard_type_png(self):
        self.filepath = clipboard_image_to_png(get_image_clipboard())
        clipboard_image = get_image_file(self.filepath)
        self.assertIsInstance(clipboard_image, PIL.PngImagePlugin.PngImageFile)

    def tearDown(self) -> None:
        set_empty_clipboard()
        os.remove(self.filepath)


class TestImageToPng(TestCase):

    def setUp(self) -> None:
        set_clipboard_image(test_image_file)

    def test_clipboard_image_to_png(self):
        self.filepath = clipboard_image_to_png(get_image_clipboard())
        self.assertTrue(os.path.isfile(self.filepath))

    def tearDown(self) -> None:
        set_empty_clipboard()
        os.remove(self.filepath)


if __name__ == '__main__':
    unittest.main()

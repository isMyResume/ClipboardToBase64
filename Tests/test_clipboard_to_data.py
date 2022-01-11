import os
import unittest
from unittest import TestCase

import PIL

from clipboard_to_base64_tag import get_clipboard_to_base64
from clipboard_to_data import clipboard_image_to_png, get_image_clipboard, is_tex, tex_to_png
from utility import set_clipboard_image, set_empty_clipboard, get_image_file, set_clipboard_text

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


test_tex = r'$RI=\frac{\pi R I \degree}{180}=0.0174333RI\degree$'
test_tex_image= 'test_tex_image.png'

class TestGetClipboardTypeIsTex(TestCase):
    def setUp(self) -> None:
        set_clipboard_text(test_tex)

    def test_get_clipboard_type_is_tex(self):
        clipboard_data = get_clipboard_to_base64()
        str_type = is_tex(clipboard_data)
        self.assertEqual(str_type, 'tex')

    def tearDown(self) -> None:
        set_empty_clipboard()


class TestTexToPng(TestCase):
    def setUp(self) -> None:
        with open(test_tex_image, 'rb') as image:
            self.test_tex_image_read = image.read()
    def test_tex_to_png(self):
        self.tex_png_image = tex_to_png(test_tex)
        with open(self.tex_png_image, 'rb') as image:
            self.tex_png_image_read = image.read()
        self.assertEqual(self.tex_png_image_read,self.test_tex_image_read)
    def tearDown(self) -> None:
        os.remove(self.tex_png_image)



if __name__ == '__main__':
    unittest.main()

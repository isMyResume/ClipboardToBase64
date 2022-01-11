import unittest
from unittest import TestCase

from data_to_base64 import pngimagefile_to_base64, convert_markdown_image_tag

test_image_file = 'animal.png'
test_base64_file = 'animal.txt'
test_markdown_tag_file = 'markdown_animal.txt'


class TestPngToBase64(TestCase):
    def setUp(self) -> None:
        with open(test_base64_file, 'r') as text:
            self.base64_text = text.read()

    def test_image_to_png(self):
        image_read = pngimagefile_to_base64(test_image_file)
        self.assertEqual(len(image_read), len(self.base64_text))


class TestConvertImageTag(TestCase):
    def setUp(self) -> None:
        self.base64_image = pngimagefile_to_base64(test_image_file)
        with open(test_markdown_tag_file, 'r') as text:
            self.base64_text = text.read()

    def test_convert_image_tag(self):
        image_tag = convert_markdown_image_tag(test_image_file, self.base64_image)
        self.assertEqual(len(image_tag), len(self.base64_text))


if __name__ == '__main__':
    unittest.main()

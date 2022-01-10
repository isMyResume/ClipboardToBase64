import unittest
from unittest import TestCase

import PIL

from utility import get_clipboard, set_clipboard_image, set_empty_clipboard


class TestGetClipboard(TestCase):
    def setUp(self):
        set_clipboard_image('animal.png')

    # FIXME : 클립보드 직접 복사시 PNG, 파일을 불러와서 win32clipboard로 넣을 때는 Bmp
    def test_get_clipboard_type_png(self):
        clipboard_image = get_clipboard()
        self.assertIsInstance(clipboard_image, PIL.BmpImagePlugin.DibImageFile)

    def tearDown(self) -> None:
        set_empty_clipboard()


if __name__ == '__main__':
    unittest.main()

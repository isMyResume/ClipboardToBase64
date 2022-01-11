# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QGridLayout, QSizePolicy

from clipboard_to_base64_tag import get_clipboard_to_base64


def clipboard_to_base64():
    get_clipboard_to_base64()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 100)
        self.copyButton = QPushButton("Copy")
        self.copyButton.clicked.connect(clipboard_to_base64)
        self.checkButton = QCheckBox("Always On")
        self.checkButton.stateChanged.connect(self.alwaysontop)
        layout = QGridLayout(self)
        self.copyButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.copyButton, 1, 0, 1, 1)
        layout.addWidget(self.checkButton, 2, 0, 1, 1)
        self.setLayout(layout)

    def alwaysontop(self, state):
        if state == Qt.Checked:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()

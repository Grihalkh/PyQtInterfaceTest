# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
import libs.lang as lang
import libs.buttonfuncs as bf
import os


class UI(QWidget):
    def __init__(self):
        super().__init__()

        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        uic.loadUi(path + '/ui/main.ui', self)

        self.set_lang(self)
        self.connect_button_funcs(self)

        self.show()

    def set_lang(self, parent_widget):
        parent_widget.setWindowTitle(lang.strings['prog_title'])
        parent_widget.enterNameLabel.setText(lang.strings['enter_name_label'])
        parent_widget.enterNameButton.setText(lang.strings['enter_name_button'])
        parent_widget.greetLabel.setText('')

    def connect_button_funcs(self, parent_widget):
        parent_widget.enterNameButton.clicked.connect(lambda: bf.enter_name_button(
            parent_widget.enterNameEdit, parent_widget.greetLabel
        ))

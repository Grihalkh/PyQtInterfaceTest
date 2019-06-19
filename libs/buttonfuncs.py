# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QLineEdit, QLabel
import libs.lang as lang


def enter_name_button(enterNameEdit: QLineEdit, greetLabel: QLabel):
    name = enterNameEdit.text()
    greetLabel.setText(lang.strings['greet_label'] + name)


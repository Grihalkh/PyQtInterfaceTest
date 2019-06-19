# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication
import libs.interface as ui
import libs.lang as lang

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lang.get_lang()
    window = ui.UI()
    sys.exit(app.exec_())

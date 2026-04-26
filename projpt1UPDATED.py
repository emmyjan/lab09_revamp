import QtDesign
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *


def main():
    app = QApplication(sys.argv)

    window = uic.loadUi("projpt1UPDATED.ui")
    window.show()
    app.exec()
# TODO needs correct password to open account if name doesn't exist, make new account
if __name__ == '__main__':
    main()

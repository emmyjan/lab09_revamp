import QtDesign
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *


def main():
    app = QApplication(sys.argv)

    window = uic.loadUi("proj2.ui")
    window.show()
    app.exec()
# TODO make an end screen for when both players pass back to back
#  add in a way to make it back to the start screen.
if __name__ == '__main__':
    main()

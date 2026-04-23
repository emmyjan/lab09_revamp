import QtDesign
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *


def main():
    app = QApplication(sys.argv)

    window = uic.loadUi("proj2.ui")
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

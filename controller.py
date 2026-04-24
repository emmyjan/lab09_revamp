from gui import *
from PyQt6.QtWidgets import *
import sys


class Controller(QMainWindow, Ui_ATM):
    super().__init__()
    QMainWindow.__init__
    
    def __init__(self, window):
        app = QtWidgets.QApplication(sys.argv)
        ATM = QtWidgets.QMainWindow()
        ui = Ui_ATM()
        ui.setupUi(ATM)
        self.show()
        sys.exit(app.exec())

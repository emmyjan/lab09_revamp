from gui import *
from PyQt6.QtWidgets import *
from accounts import *

class Controller(QMainWindow, Ui_ATM):

    def __init__(self, app: QApplication):
        super().__init__()
        self.setupUi(self)
        self.app = app
        
        self.Enter.clicked.connect(self.submit_input)
        self.Exit.clicked.connect(app.quit)
    """
    TODO:In projpt1UPDATED.ui, change the four entry fields to QLineEdit
    """
    def get_inputs(self):
        """Returns a tuple of: First Name, Last Name, PIN, and Amount"""
        acc_first_name = self.INFNAME.toPlainText()
        acc_last_name = self.INLNAME.toPlainText()
        acc_pin = self.INPIN.toPlainText()
        acc_amt = self.INAMOUNT.toPlainText()

        return (acc_first_name, acc_last_name, acc_pin, acc_amt)
    
    def submit_input(self):
        vals = self.get_inputs()
        print(vals)
    

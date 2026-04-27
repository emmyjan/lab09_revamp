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

    def get_inputs(self):
        """Returns a tuple of: First Name, Last Name, PIN, and Amount"""
        acc_first_name = self.lineEdit.text()
        acc_last_name = self.LNAMEIN.text()
        acc_pin = self.PASSIN.text()
        acc_amt = self.AMIN.text()

        return (acc_first_name, acc_last_name, acc_pin, acc_amt)
    
    def submit_input(self):
        vals = self.get_inputs()
        name = vals[0] + vals[1]
        password = vals[2]
        balance = float(vals[3])
        for val in vals:
            if val == '':
                print("UserError: Not all fields entered")
                return
        acc = Account.find_global_account(name)
        if acc == None:
            print("No account found. Creating new account")
            acc = Account(name, balance, password=password)
            acc.write_to_csv("bank.csv")
            return
        print(acc)
        print(vals)
    

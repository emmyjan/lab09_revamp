from gui import *
from PyQt6.QtWidgets import *
from accounts import *

class Controller(QMainWindow, Ui_ATM):

    WITHDRAW_CHECKED = 0
    DEPOSIT_CHECKED = 1
    NONE_CHECKED = 2

    VAL_FNAME = 0
    VAL_LNAME = 1
    VAL_PWORD = 2
    VAL_BAL = 3

    def __init__(self, app: QApplication):
        super().__init__()
        self.setupUi(self)
        Account.populate_accounts("bank.csv")
        self.app = app
        self.Search.clicked.connect(self.search_button)
        self.Exit.clicked.connect(self.exit_button)
        self.Enter.clicked.connect(self.submit_button)

    def exit_button(self):
        Account.write_all_accounts_to_csv("bank.csv")
        Account.print_global_accounts()
        self.app.quit()

    def get_radio_choice(self):
        """Returns a number corresponing to either WITHDRAW_CHECKED or DEPOSIT_CHECKED or NONE_CHECKED"""
        if self.Withdraw.isChecked():
            return self.WITHDRAW_CHECKED
        elif self.Deposit.isChecked():
            return self.DEPOSIT_CHECKED
        else:
            return self.NONE_CHECKED

    def get_inputs(self):
        """Returns a tuple of: First Name, Last Name, PIN, and Amount"""
        acc_first_name = self.lineEdit.text()
        acc_last_name = self.LNAMEIN.text()
        acc_pin = self.PASSIN.text()
        acc_amt = self.AMIN.text()

        return (acc_first_name, acc_last_name, acc_pin, acc_amt)
    
    def set_output_text(self, text: str):
        """Sets the text of the output-to-user label"""
        self.output_label.setText(text)

    def clear(self):
        self.set_output_text("")

    def search_button(self) -> Account|SavingAccount:
        """Returns either an existing Account or new Account depending on
           if one exists in the global Account list 
        """
        vals = self.get_inputs()
        name = vals[self.VAL_FNAME] + vals[self.VAL_LNAME]
        password = vals[self.VAL_PWORD]

        # try:
        #     balance = float(vals[3])
        # except ValueError: #Ensure that balance is in float/int format
        #     self.set_output_text("UserError: Invalid balance input")
        #     return None
            
        # for val in vals: #Ensure that user has filled out all fields
        #     if val == '':
        #         self.set_output_text("UserError: Not all fields entered")
        #         return None

        acc = Account.find_global_account(name)
        if acc == None: #Create account if one does not already exist in global array
            self.set_output_text("No account found. Creating new account")
            acc = Account(name, password=password)
            acc.write_to_csv("bank.csv")
            return acc
        else:
            type = "Saving Account" if acc.__class__ == SavingAccount else "Account" 
            self.set_output_text(f"Welcome, {vals[self.VAL_FNAME]} {vals[self.VAL_LNAME]}!\nYou currently have ${acc.get_balance():.2f} in your {type}.")
        
    def submit_button(self):
        vals = self.get_inputs()
        acc = Account.find_global_account(vals[self.VAL_FNAME] + vals[self.VAL_LNAME])

        if acc == None: #Error Case
            self.search_button()
            return
        choice = self.get_radio_choice()
        try:
            if choice == self.NONE_CHECKED: #Error Case
                self.set_output_text("UserError: No choice")
                return
            elif choice == self.DEPOSIT_CHECKED:
                acc.deposit(float(vals[self.VAL_BAL]))
                self.set_output_text(f"Deposited!\nYour new balance is {acc.get_balance()}.")
            elif choice == self.WITHDRAW_CHECKED:
                acc.withdraw(float(vals[self.VAL_BAL]))
                self.set_output_text(f"Dispensed ${float(vals[self.VAL_BAL])}!\nYour new balance is {acc.get_balance()}.")
        except ValueError:
            self.set_output_text("UserError: Invalid balance")

        
    

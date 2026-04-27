import csv


class Account:
    __global_accounts = []

    def __init__(self, name, balance=0, password="password"):
        self.__account_name = name
        self.__account_balance = balance
        self.set_balance(balance)
        self.__password = password
        self.__global_accounts.append(self)
        
    def print_global_accounts():
        
        for ac in Account.__global_accounts:
            print(ac.get_name())
            
        print(Account.__global_accounts)

    def write_all_accounts_to_csv(filename: str):
        """Overwrites contents of filename and write all existing Accounts to filename"""
        with open(filename, "w") as cfile:
            for acc in Account.__global_accounts:
                write = csv.writer(cfile, lineterminator="\n")
                write.writerow([acc.get_name(), acc.get_balance(), acc.get_password(), acc.__class__])

    def populate_accounts(filename: str):
        """Populates __global_accounts with Accounts in CSV file"""
        Account.__global_accounts = []
        with open(filename) as cfile:
            read = csv.reader(cfile, delimiter=",", lineterminator='\n')
            for line, row in enumerate(read):
                #Attempt to create either a new Account or SavingAccount
                try:
                    if len(row) == 3 or row[3] == "<class 'accounts.Account'>":
                        Account(row[0],balance=float(row[1]),password=row[2])
                    elif row[3] == "<class 'accounts.SavingAccount'>":
                        save_acc = SavingAccount(row[0])
                        save_acc.set_balance(float(row[1]))
                        save_acc.set_password(row[2])                        
                except IndexError:
                    print(f"Error in CVS formatting on line {line}")
                except ValueError:
                    print(f"Error in CVS formatting on line {line}")                    
        
    def deposit(self, amount) -> bool:
        """Withdraws certain amount from Account. Returns True if successful."""
        if amount <= 0:
            return False
        
        self.set_balance(self.__account_balance + amount)
        return True
    
    def withdraw(self, amount) -> bool:
        """Withdraws certain amount from Account. Returns True if successful."""
        if amount <= 0 or amount > self.get_balance():
            return False
        
        self.set_balance(self.get_balance() - amount)
        return True
    
    def write_to_csv(self, filename):
        """Writes Account instance to CSV"""
        with open(filename, 'a') as cfile:
            write = csv.writer(cfile, lineterminator="\n")
            write.writerow([self.get_name(), self.get_balance(), self.get_password(), self.__class__])

    def check_password(self, password: str) -> bool:
        return password == self.__password
    
    def get_balance(self):
        return self.__account_balance
    
    def get_name(self):
        return self.__account_name

    #This feels so wrong to write
    def get_password(self):
        return self.__password
    
    def find_global_account(name: str):
        """Returns Account instance if name matches, otherwise None"""
        for acc in Account.__global_accounts:
            if acc.get_name() == name:
                return acc
        return None
    
    def set_password(self, password):
        self.__password = password

    def set_balance(self, value):
        self.__account_balance = value if value > 0 else 0

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"Account name = {self.__account_name}, Account balance = {(self.__account_balance):.2f}"

class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name):
        super().__init__(name)
        super().set_balance(self.MINIMUM)
        self.__deposit_count = 0

    #Applies the RATE as interest
    def apply_interest(self):
        bal = self.get_balance()
        self.set_balance(bal + (bal * self.RATE))
        
    def deposit(self, amount):
        if amount <= 0:
            return False
        
        super().deposit(amount)
        self.__deposit_count += 1

        if self.__deposit_count % 5 == 0:
            self.apply_interest()

        return True
    
    def withdraw(self, amount):
        #Check to ensure balance does not go below minimum
        if amount > (self.get_balance() - self.MINIMUM):
            return False
        elif self.get_balance() < amount:
            return False
        elif amount <= 0:
            return False
        
        return super().withdraw(amount)

    def set_balance(self, amount):
        #Check to ensure balance does not go below minimum
        if amount < self.MINIMUM:
            super().set_balance(self.MINIMUM)
            return
            
        super().set_balance(amount)
    
    def __str__(self):
        return f"SAVING ACCOUNT: {super().__str__()}"

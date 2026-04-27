from accounts import *


Account.populate_accounts("bank.csv")
Account.print_global_accounts()
#sa.write_to_csv("bank.csv")
print(Account.find_global_account("glorbiam"))
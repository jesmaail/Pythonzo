from ApiLayer import MonzoApiLayer
from Monzo import Monzo, MonzoAccount, MonzoBalance, MonzoTransaction, MonzoTransactions
import os

# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = MonzoApiLayer(accessToken)

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Monzo Super Object
myMonzo = Monzo(accessToken)

print("Monzo Super Object:")
print("Account ID: " + myMonzo.get_account_id())
print("Account Holder: " + myMonzo.get_account_holder())
print("Balance: " + myMonzo.get_current_balance())
print("No. of Transactions: " + str(myMonzo.transactions.transactions_num))
print("No. of Payments: " + str(len(myMonzo.transactions.get_all_payments())))
print("No. of Topups: " + str(len(myMonzo.transactions.get_all_topups())))
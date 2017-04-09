from ApiLayer import MonzoApiLayer
from Monzo import Monzo, MonzoAccount, MonzoBalance, MonzoTransaction, MonzoTransactions
import os

# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = MonzoApiLayer(accessToken)

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')


def printNumberedList(list):
	for x in range(0, len(list)):
		print(str(x) + ". " + list[x])


# Monzo Super Object
myMonzo = Monzo(accessToken)
transactions = myMonzo.transactions

paymentsNum = len(transactions.get_all_payments())
topupsNum = len(transactions.get_all_topups())
merchantNames = transactions.get_list_of_merchant_names()
categories = transactions.get_list_of_categories()

print("Monzo Super Object:")
print("Account ID: " + myMonzo.get_account_id())
print("Account Holder: " + myMonzo.get_account_holder())
print("Balance: " + myMonzo.get_current_balance())
print("No. of Transactions: " + str(transactions.transactions_num))
print("No. of Payments: " + str(paymentsNum))
print("No. of Topups: " + str(topupsNum))
print("\nMerchants: ")
print(printNumberedList(merchantNames))
print("\nCategories: ")
print(printNumberedList(categories))
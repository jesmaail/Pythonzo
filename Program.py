from ApiLayer import MonzoApiLayer
from Monzo import Monzo
import os

# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = MonzoApiLayer(accessToken)

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')


def printNumberedList(list):
	for x in range(0, len(list)):
		print(str(x) + ". " + list[x])

def printTransaction(transaction):
	print("ID: " + str(transaction.id))
	print("Date: " + str(transaction.time.get_formatted_datetime()))
	print("Merchant: " + str(transaction.merchant.name))
	print("Category: " + str(transaction.merchant.category))
	print("Amount: " + str(transaction.get_formatted_amount()))

def printTransactionList(transactions):
	for transaction in transactions:
		printTransaction(transaction)
		print("")


# Monzo Super Object
myMonzo = Monzo(accessToken)
transactions = myMonzo.transactions

payments = myMonzo.get_all_payments()
topups = myMonzo.get_all_topups()

paymentsNum = len(payments)
topupsNum = len(topups)
merchantNames = myMonzo.get_merchants_names()
categories = myMonzo.get_categories()
paymentsThisWeek = myMonzo.get_payments_by_date("2017-04-10", "2017-04-16")
numPaymentsThisWeek = len(paymentsThisWeek)
entertainmentTransactions = myMonzo.get_payments_by_category("entertainment")
numEntertainmentTransactions = len(entertainmentTransactions)
merchantTransactions = myMonzo.get_payments_by_merchant("The Reverend James")

criteriaList = [entertainmentTransactions, paymentsThisWeek, merchantTransactions]

print("Monzo Super Object:")
print("Account ID: " + myMonzo.get_account_id())
print("Account Holder: " + myMonzo.get_account_holder())
print("Balance: " + myMonzo.get_current_balance())
print("No. of Transactions: " + str(transactions.transactions_num))
print("No. of Payments: " + str(paymentsNum))
print("No. of Topups: " + str(topupsNum))

print("\nPayments by date and category:\n")
printTransactionList(myMonzo.get_multiple_criteria(criteriaList))


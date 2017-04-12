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

def printTransaction(transaction):
	print("ID: " + str(transaction.id))
	print("Date: " + str(transaction.date))
	print("Merchant: " + str(transaction.merchant.name))
	print("Amount: " + str(transaction.get_formatted_amount()))

def printTransactionList(transactions):
	for transaction in transactions:
		printTransaction(transaction)
		print("")


# Monzo Super Object
myMonzo = Monzo(accessToken)
transactions = myMonzo.transactions

payments = transactions.get_all_payments()
topups = transactions.get_all_topups()

paymentsNum = len(payments)
topupsNum = len(topups)
merchantNames = transactions.get_list_of_merchant_names()
categories = transactions.get_list_of_categories()
paymentsThisWeek = transactions.get_payments_by_date_range("2017-04-10", "2017-04-16")
numPaymentsThisWeek = transactions.get_num_payments_at_date_range("2017-04-10", "2017-04-16")

print("Monzo Super Object:")
print("Account ID: " + myMonzo.get_account_id())
print("Account Holder: " + myMonzo.get_account_holder())
print("Balance: " + myMonzo.get_current_balance())
print("No. of Transactions: " + str(transactions.transactions_num))
print("No. of Payments: " + str(paymentsNum))
print("No. of Topups: " + str(topupsNum))

print("Payments This Week:\n")
printTransactionList(paymentsThisWeek)

print("No. of Payments This Week: " + str(numPaymentsThisWeek))

# print("\nMerchants: ")
# printNumberedList(merchantNames)
# print("\nCategories: ")
# printNumberedList(categories)

#print(transactions.get_payment_by_merchant_name("KFC"))
#print("Fried Chicken count: " + str(transactions.get_num_payments_at_merchant("KFC")))
from ApiLayer import MonzoApiLayer
from Monzo import Monzo, MonzoAccount, MonzoBalance, MonzoTransaction, MonzoTransactions
import os

# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = MonzoApiLayer(accessToken)

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')


# These next bits will be gone when moving to the Monzo Object for holding all the information.
myAccount = MonzoAccount(api.get_accounts())
accountId = myAccount.id

print("Test Data:")

myBalance = MonzoBalance(api.get_balance(accountId))
print("Balance: " + myBalance.get_formatted_amount())

myFirstTransaction = MonzoTransaction(api.get_transactions(accountId)[3])
print("Transaction 3 Amount: " + myFirstTransaction.get_formatted_amount())
#print(myFirstTransaction.merchant.name)

myTransactionsOld = api.get_transactions(accountId)
print("Old Transaction method length: " + str(len(myTransactionsOld)))
print("Old Transaction method TopUp check: " + str(myTransactionsOld[1]['is_load']))

myTransactionsNew = MonzoTransactions(api.get_transactions(accountId))
#print("New Transaction method length: " + str(myTransactionsNew.get_transactions_num()))
#print("New Transaction method transaction Merchant: " + str(myTransactionsNew.get_transaction_at_index(0).merchant))
#print("Payments Count: " + str(len(myTransactionsNew.get_all_payments())))
#print("TopUps Count: " + str(len(myTransactionsNew.get_all_topups())))
print("T: " + str(len(myTransactionsNew.topups)))
print("P: " + str(len(myTransactionsNew.payments)))


# Monzo Super Object
myMonzo = Monzo(accessToken)

print("\nMonzo Super Object:")
print("Account ID: " + myMonzo.get_account_id())
print("Account Holder: " + myMonzo.get_account_holder())
print("Balance: " + myMonzo.get_current_balance())
print("No. of Transactions: " + str(myMonzo.get_transactions_num()))
print("No. of Payments: " + str(len(myMonzo.get_all_payments())))
print("No. of Topups: " + str(len(myMonzo.get_all_topups())))
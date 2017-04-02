from ApiLayer import MonzoApiLayer
from Monzo import Monzo, MonzoAccount, MonzoBalance, MonzoTransaction
import os

# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = MonzoApiLayer(accessToken)

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')


# These next bits will be gone when moving to the Monzo Object for holding all the information.
myAccount = MonzoAccount(api.get_accounts())
accountId = myAccount.id
myBalance = MonzoBalance(api.get_balance(accountId))
myFirstTransaction = MonzoTransaction(api.get_transactions(accountId)['transactions'][3])

print("Test Data:")
print(myBalance.get_formatted_amount())
print(myFirstTransaction.get_formatted_amount())
print(myFirstTransaction.merchant.name)


# Monzo Super Object
myMonzo = Monzo(accessToken)

print("\nMonzo Super Object:")
print("Account ID: " + myMonzo.account_id)
print("Account Holder: " + myMonzo.account_holder)
print("Balance: " + myMonzo.balance)
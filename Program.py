from ApiLayer import MonzoApiLayer
from Monzo import Monzo, MonzoAccount, MonzoBalance, MonzoTransaction
import os

# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = MonzoApiLayer(accessToken)

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')


# These next bits will be gone when moving to the Monzo Object for holding all the information.
myAccount = MonzoAccount(api.GetAccounts())
accountId = myAccount.ID
myBalance = MonzoBalance(api.GetBalance(accountId))
myFirstTransaction = MonzoTransaction(api.GetTransactions(accountId)['transactions'][3])
print("Test Data")
print(myBalance.GetFormattedAmount())
print(myFirstTransaction.GetFormattedAmount())
print(myFirstTransaction.MERCHANT.NAME)


# Monzo Super Object
myMonzo = Monzo(accessToken)

print("\nMonzo Super Object:")
print("Account ID: " + myMonzo.ACCOUNT_ID)
print("Account Holder: " + myMonzo.ACCOUNT_HOLDER)
print("Balance: " + myMonzo.BALANCE)



## Bits that have been used to verify functionality
#print(api.GetTransactions(accountId)['transactions'][0])
#print(myBalance.BALANCE)
#print("Account Id: " + myAccount.ID)
#print("Account Creation Date: " + myAccount.CREATED)
#print("Account Description: " + myAccount.DESCRIPTION)
#print("")
#print(api.WhoAmI())
#print(api.GetBalance(accountId)['balance'])
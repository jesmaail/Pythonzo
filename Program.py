from ApiLayer import MonzoApiLayer
from Monzo import MonzoAccount, MonzoBalance, MonzoTransaction
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

print(myBalance.GetFormattedAmount())
print(myFirstTransaction.GetFormattedAmount())
print(myFirstTransaction.MERCHANT.NAME)



## Bits that have been used to verify functionality
#print(api.GetTransactions(accountId)['transactions'][0])
#print(myBalance.BALANCE)
#print("Account Id: " + myAccount.ID)
#print("Account Creation Date: " + myAccount.CREATED)
#print("Account Description: " + myAccount.DESCRIPTION)
#print("")
#print(api.WhoAmI())
#print(api.GetBalance(accountId)['balance'])
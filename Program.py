from ApiLayer import MonzoApiLayer
from Monzo import MonzoAccount, MonzoBalance
import os

# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = MonzoApiLayer(accessToken)

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')


myAccount = MonzoAccount(api.GetAccounts())
accountId = myAccount.ID

myBalance = MonzoBalance(api.GetBalance(accountId))

print(myBalance.BALANCE)
print(myBalance.GetFormattedBalance())


#print("Account Id: " + myAccount.ID)
#print("Account Creation Date: " + myAccount.CREATED)
#print("Account Description: " + myAccount.DESCRIPTION)
#print("")
#print(api.WhoAmI())

#print(api.GetBalance(accountId)['balance'])
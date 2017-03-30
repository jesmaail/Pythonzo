import requests, os

# Object that handles API communication, ideally want to move to some inheritance
class ApiLayer(object):
	MONZO_URL = 'https://api.monzo.com'

	## Constructor, will take in an access token, and generate the auth header.
	def __init__(self, token):
		self.ACCESS_TOKEN = token		
		self.HEADERS = {'Authorization': 'Bearer {0}'.format(self.ACCESS_TOKEN)}

	def GetAccounts(self):
		return self.Get(self.MONZO_URL + "/accounts", self.HEADERS)

	def WhoAmI(self):
		return self.Get(self.MONZO_URL + "/ping/whoami", self.HEADERS)

	def GetTransactions(self, account_id):
		return self.Get(self.MONZO_URL + "/transactions?expand[]=merchant&account+id=" + account_id, self.HEADERS)

	def GetBalance(self, account_id):
		return self.Get(self.MONZO_URL + "/balance?account_id=" + account_id, self.HEADERS)


	def Get(self, url, headers=None, params=None):
		response = requests.get(url=url, headers=headers, params=params)
		return self.Validate(response)

	def Post(self, url, headers=None, params=None, data=None):
		response = requests.post(url=url, headers=headers, data=data, params=params)
		return self.Validate(response)

	# Want to make sure we are getting OK response
	def Validate(self, response):
		if response.status_code == 200:
			return response.json()
		else:
			print("Failure:")
			return response


# Holds Account information
class MonzoAccount(object):

	def __init__(self, acc):
		self.ID = acc['accounts'][0]['id']
		self.CREATED = acc['accounts'][0]['created']
		self.DESCRIPTION = acc['accounts'][0]['description']

# Holds Account Balance information
class MonzoBalance(object):

	def __init__(self, bal):
		self.BALANCE = bal['balance']
		self.CURRENCY = bal['currency']
		self.SPEND_TODAY = bal['spend_today']
		self.LOCAL_CURRENCY = bal['local_currency']
		self.LOCAL_EXCHANGE_RATE = bal['local_exchange_rate']

	def GetFormattedBalance(self):
		return {
			"GBP" : "£" + str(self.BALANCE /100)
		}[self.CURRENCY]




# Take in the access token for access to account
accessToken = input("Enter Monzo access token: ")
api = ApiLayer(accessToken)

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
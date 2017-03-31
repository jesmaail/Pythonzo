import requests

# Object that handles API communication, ideally want to move to some inheritance
class ApiLayer:
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
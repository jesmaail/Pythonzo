import requests

class ApiLayer(object):

	## Constructor, will take in an access token, and generate the auth header.
	def __init__(self, token):
		self.ACCESS_TOKEN = token		
		self.HEADERS = {'Authorization': 'Bearer {0}'.format(self.ACCESS_TOKEN)}		

	def get(self, url, headers=None, params=None):
		response = requests.get(url=url, headers=headers, params=params)
		return self.validate(response)

	def post(self, url, headers=None, params=None, data=None):
		response = requests.post(url=url, headers=headers, data=data, params=params)
		return self.validate(response)

	# Want to make sure we are getting OK response
	def validate(self, response):
		if response.status_code == 200:
			return response.json()
		else:
			print("Failure:")
			return response


class MonzoApiLayer(ApiLayer):

	MONZO_URL = 'https://api.monzo.com'
	ACCOUNTS_URL = "/accounts"
	WHOAMI_URL = "/ping/whoami"
	TRANSACTIONS_URL = "/transactions?expand[]=merchant&account_id="
	BALANCE_URL = "/balance?account_id="

	def get_accounts(self):
		return self.get(self.MONZO_URL + self.ACCOUNTS_URL, self.HEADERS)

	def who_am_I(self):
		return self.get(self.MONZO_URL + self.WHOAMI_URL, self.HEADERS)

	def get_transactions(self, account_id):
		return self.get(self.MONZO_URL + self.TRANSACTIONS_URL + account_id, self.HEADERS)['transactions']

	def get_balance(self, account_id):
		return self.get(self.MONZO_URL + self.BALANCE_URL + account_id, self.HEADERS)
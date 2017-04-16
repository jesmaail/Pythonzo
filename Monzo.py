from ApiLayer import MonzoApiLayer
from MonzoCommon import MonzoAccount, MonzoBalance
from MonzoTransactions import MonzoTransactions

# Class that will hold everything, pass in the access token here.
#
# ToDo:
#	- Multiple query criteria at once
#	- Format Dates into Date and Time
#	- Unit tests?
#	- Be able to query the transactions by date, merchant, category
#	
class Monzo(object):

	def __init__(self, token):
		monzoApi = MonzoApiLayer(token)
		self.account = MonzoAccount(monzoApi.get_accounts())
		self.balance = MonzoBalance(monzoApi.get_balance(self.get_account_id()))
		self.transactions = MonzoTransactions(monzoApi.get_transactions(self.get_account_id()))

	def get_account_id(self):
		return self.account.id

	def get_account_holder(self):
		return self.account.description

	def get_current_balance(self):
		return self.balance.get_formatted_amount()

from ApiLayer import MonzoApiLayer
from MonzoCommon import MonzoAccount, MonzoBalance
from MonzoTransactions import MonzoTransactions

# Class that will hold everything, pass in the access token here.
#
# ToDo:
#	- Move Queries into the Monzo Object?
#	- Unit tests?
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

	def get_all_payments(self):
		return NotImplementedError

	def get_all_topups(self):
		return NotImplemented

	def get_merchants_names(self):
		return NotImplemented

	def get_categories(self):
		return NotImplemented

	def get_payments_by_merchant(self, merchant_name):
		return NotImplemented

	def get_payments_by_category(self, category):
		return NotImplemented

	def get_payments_by_date(self, start_date, end_date):
		return NotImplemented

	def get_multiple_criteria(self, criteria_list):
		return NotImplemented
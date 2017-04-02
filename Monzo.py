from ApiLayer import MonzoApiLayer

# Common methods across Monzo classes
class CurrencyObject(object):

	def get_formatted_amount(self):
		return {
			"GBP" : "£" + str(format(self.amount /100, '.2f'))
		}[self.currency]

# Holds Account information
class MonzoAccount(object):

	def __init__(self, acc):
		self.id = acc['accounts'][0]['id']
		self.created = acc['accounts'][0]['created']
		self.description = acc['accounts'][0]['description']


# Holds Account Balance information
class MonzoBalance(CurrencyObject):

	def __init__(self, bal):
		self.amount = bal['balance']
		self.currency = bal['currency']
		self.spend_today = bal['spend_today']
		self.local_currency = bal['local_currency']
		self.local_exchange_rate = bal['local_exchange_rate']


# Holds Transaction information
class MonzoTransaction(CurrencyObject):

	def __init__(self, tran):
		self.id = tran['id']
		self.date = tran['created']
		self.merchant = MonzoMerchant(tran['merchant'])
		self.amount = tran['local_amount']
		self.currency = tran['local_currency']
		self.is_topup = tran['is_load']


# Holds Merchant information
class MonzoMerchant(object):

	def __init__(self, merch):
		self.id = merch['id']
		self.group_id = merch['group_id']
		self.name = merch['name']
		self.category = merch['category']


# Class that will hold everything, pass in the access token here.
#
# ToDo:
#	- Move the AccountID, AccountHolder, Balance, etc. to Getter Methods
#	- Add a transactions object holding all transactions
#	- Be able to query the transactions by date, merchant, category
#
class Monzo(object):

	def __init__(self, token):
		monzoApi = MonzoApiLayer(token)

		self.account_object = MonzoAccount(monzoApi.get_accounts())
		self.account_id = self.account_object.id
		self.account_holder = self.account_object.description

		self.balance_object = MonzoBalance(monzoApi.get_balance(self.account_id)) 
		self.balance = self.balance_object.get_formatted_amount()
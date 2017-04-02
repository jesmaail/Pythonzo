from ApiLayer import MonzoApiLayer

# Common methods across Monzo classes
class CurrencyObject(object):

	def GetFormattedAmount(self):
		return {
			"GBP" : "£" + str(format(self.AMOUNT /100, '.2f'))
		}[self.CURRENCY]

# Holds Account information
class MonzoAccount(object):

	def __init__(self, acc):
		self.ID = acc['accounts'][0]['id']
		self.CREATED = acc['accounts'][0]['created']
		self.DESCRIPTION = acc['accounts'][0]['description']


# Holds Account Balance information
class MonzoBalance(CurrencyObject):

	def __init__(self, bal):
		self.AMOUNT = bal['balance']
		self.CURRENCY = bal['currency']
		self.SPEND_TODAY = bal['spend_today']
		self.LOCAL_CURRENCY = bal['local_currency']
		self.LOCAL_EXCHANGE_RATE = bal['local_exchange_rate']


# Holds Transaction information
class MonzoTransaction(CurrencyObject):

	def __init__(self, tran):
		self.ID = tran['id']
		self.DATE = tran['created']
		self.MERCHANT = MonzoMerchant(tran['merchant'])
		self.AMOUNT = tran['local_amount']
		self.CURRENCY = tran['local_currency']
		self.IS_TOPUP = tran['is_load']


# Holds Merchant information
class MonzoMerchant(object):

	def __init__(self, merch):
		self.ID = merch['id']
		self.GROUP_ID = merch['group_id']
		self.NAME = merch['name']
		self.CATEGORY = merch['category']


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

		self.ACCOUNT_OBJECT = MonzoAccount(monzoApi.GetAccounts())
		self.ACCOUNT_ID = self.ACCOUNT_OBJECT.ID
		self.ACCOUNT_HOLDER = self.ACCOUNT_OBJECT.DESCRIPTION

		self.BALANCE_OBJECT = MonzoBalance(monzoApi.GetBalance(self.ACCOUNT_ID)) 
		self.BALANCE = self.BALANCE_OBJECT.GetFormattedAmount()
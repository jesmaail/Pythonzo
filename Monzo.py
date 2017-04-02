
# Common methods across these objects
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


# Class that will hold everything
class Monzo(object):

	def __init__(self, account, balance, transactions):
		self.ACCOUNT = MonzoAccount(account)

		# This needs the accountId which is part of the MonzoAccount
		#self.BALANCE = MonzoBalance(balance)


		# Need some logic here to loop over all the transactions are store in a list.

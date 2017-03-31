
# Common methods across these objects
class MonzoObject(object):

	def GetFormattedBalance(self):
		return {
			"GBP" : "£" + str(self.BALANCE /100)
		}[self.CURRENCY]


# Holds Account information
class MonzoAccount(object):

	def __init__(self, acc):
		self.ID = acc['accounts'][0]['id']
		self.CREATED = acc['accounts'][0]['created']
		self.DESCRIPTION = acc['accounts'][0]['description']


# Holds Account Balance information
class MonzoBalance(MonzoObject):

	def __init__(self, bal):
		self.BALANCE = bal['balance']
		self.CURRENCY = bal['currency']
		self.SPEND_TODAY = bal['spend_today']
		self.LOCAL_CURRENCY = bal['local_currency']
		self.LOCAL_EXCHANGE_RATE = bal['local_exchange_rate']

# Holds Transaction information
class MonzoTransaction(MonzoObject):

	def __init__(self, tran):
		self.ID = tran['id']
		self.GROUP_ID = tran['group_id']
		self.DATE = tran['created']
		self.NAME = tran['name']
		self.CATEGORY = tran['category']
		self.AMOUNT = tran['local_amount']
		self.CURRENCY = tran['local_currency']
		self.IS_TOPUP = tran['is_load']

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
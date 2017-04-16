from ApiLayer import MonzoApiLayer

# Common methods across Monzo classes
class CurrencyObject(object):

	def get_formatted_amount(self):
		currencyString = str(format(abs(self.amount/100), '.2f'))
		return {
			"GBP" : "£" + currencyString,
			"EUR" : "€" + currencyString,
			"USD" : "$" + currencyString
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
		self.datetime = MonzoTime(tran['created'])
		self.is_topup = tran['is_load']
		self.merchant = self.get_merchant_data(tran)
		self.amount = tran['local_amount']
		self.currency = tran['local_currency']

	def get_merchant_data(self, tran):
		if not self.is_topup:
			return MonzoMerchant(tran['merchant'])
		else:
			return None


# Holds transaction time information
class MonzoTime(object):

	def __init__(self, datetime):
		self.day = datetime[8:10]
		self.month = datetime[5:7]
		self.year = datetime[0:4]
		self.time = datetime[11:16]

	def get_formatted_month(self):
		return {
			"01" : "January",
			"02" : "February",
			"03" : "March",
			"04" : "April",
			"05" : "May",
			"06" : "June",
			"07" : "July",
			"08" : "August",
			"09" : "September",
			"10" : "October",
			"11" : "November",
			"12" : "December"
		}[self.month]

	def get_formatted_date(self):
		return self.day +"/"+ self.month +"/"+ self.year

	def get_formatted_datetime(self):
		return self.time +" "+ self.get_formatted_date()


# Holds Merchant information
class MonzoMerchant(object):

	def __init__(self, merch):
		self.id = merch['id']
		self.group_id = merch['group_id']
		self.name = merch['name']
		self.category = merch['category']
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
		self.is_topup = tran['is_load']
		self.merchant = self.get_merchant_data(tran)
		self.amount = tran['local_amount']
		self.currency = tran['local_currency']

	def get_merchant_data(self, tran):
		if not self.is_topup:
			return MonzoMerchant(tran['merchant'])
		else:
			return None

# # Not used currently, differentiate within the Transaction class
# class MonzoTopUp(MonzoTransaction):

# 	def get_merchant_data(self):
# 		return None


# class MonzoPayment(MonzoTransaction):

# 	def get_merchant_data(self):
# 		return MonzoMerchant(tran['merchant'])


# Holds all transactions
class MonzoTransactions(object):

	def __init__(self, trans):
		self.transactions_num = len(trans)
		self.transactions = []
		self.topups = []
		self.payments = []

		for x in range(0, self.transactions_num):
			transaction = MonzoTransaction(trans[x])
			self.transactions.append(transaction)

		self.seperate_payments_topups()

	def get_transaction_at_index(self, index):
		return self.transactions[index]

	def seperate_payments_topups(self):
		for x in range(0, self.transactions_num):
			currentTransaction = self.transactions[x]
			if currentTransaction.merchant == None:
				self.topups.append(currentTransaction)
			else:
				self.payments.append(currentTransaction)



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
# 	- Take the get Payments/Topups logic out of Monzo object (SRP and all that jazz)
#	- Store Payments and Topups seperately in the MonzoTransactions object
#	- List all merchants
#	- List all categories (Enum? but may change over time, could do it dynamically)
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

	def get_transactions_num(self):
		return self.transactions.transactions_num

	def get_all_payments(self):
		payments = []
		for x in range(0, self.get_transactions_num()):
			currentTransaction = self.transactions.get_transaction_at_index(x)
			if currentTransaction.merchant != None:
				payments.append(currentTransaction)
		return payments

	def get_all_topups(self):
		topups = []
		for x in range(0, self.get_transactions_num()):
			currentTransaction = self.transactions.get_transaction_at_index(x)
			if currentTransaction.merchant == None:
				topups.append(currentTransaction)
		return topups

from MonzoCommon import MonzoTransaction

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
		for transaction in self.transactions:
			if transaction.merchant == None:
				self.topups.append(transaction)
			else:
				self.payments.append(transaction)

	def get_all_payments(self):
		return self.payments

	def get_all_topups(self):
		return self.topups

	def get_list_of_merchant_names(self):
		merchants = []
		for payment in self.payments:
			merchants.append(payment.merchant.name)

		uniqueMerchants = set(merchants)

		return list(uniqueMerchants);

	def get_list_of_categories(self):
		categories = []
		for payment in self.payments:
			categories.append(payment.merchant.category)

		uniqueCategories = set(categories)

		return list(uniqueCategories);

	def get_payments_by_merchant_name(self, name):
		criteria = []
		for payment in self.payments:
			if payment.merchant.name == name:
				criteria.append(payment)

		return criteria

	def get_payments_by_date_range(self, start, end):
		criteria = []
		for payment in self.payments:
			if payment.time.raw > start and payment.time.raw < end:
				criteria.append(payment)

		return criteria

	def get_payments_by_category(self, category):
		criteria = []
		for payment in self.payments:
			if payment.merchant.category == category:
				criteria.append(payment)

		return criteria

	def get_multiple_criteria(self, criteriaList):
		result = set(criteriaList[0])
		for criteria in criteriaList[1:]:
		    result.intersection_update(criteria)
		return result
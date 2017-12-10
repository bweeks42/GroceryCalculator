class Person:
	"""Someone who lives at Lawrence"""
	def __init__(self, name):
		self.name = name
		self.items = []
		self.balance = 0
	def addItem(self, item):
		self.items.append(item)
	def totalItemPrice(self):
		total = 0
		for item in self.items:
			total += item.price
		return total

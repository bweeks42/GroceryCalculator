class Item:
	"""An item purchased by a Legends"""
	def __init__(self, elements):
		
		self.price = float(elements[0])
		self.abstainers = []
		for element in elements[1:]:
			self.abstainers.append(element.strip("\n"))

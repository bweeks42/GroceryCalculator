from item import Item
from math import *
from person import Person

def main():
	persons = read_items("ItemList.txt")

	# calculate total owed
	for person in persons:
		for item in person.items:
			div = 6 - len(item.abstainers)
			price = item.price / div
			for person2 in persons:
				if person2.name not in item.abstainers:
					person2.balance += price			
	# subtract paid
	for person in persons:
		person.balance -= person.totalItemPrice()
		print(person.name + " Spent: " + str(person.totalItemPrice()) + " Balance: " + str(person.balance))


def read_items(file_name):
	legends = ["BW", "CB", "TL", "JW", "AS", "IT"]	
	persons = []

	for legend in legends:
		persons.append(Person(legend))

	f = open(file_name, "r") #opens file as read only
	buyer = None
	counted_subtotal = 0
	claimed_subtotal = 0

	for line in f:
		elements = line.split(" ")
		if (elements[0] == "\n"):
			continue
		elif (buyer == None):
			buyer_name = line.split(" ")[2].strip("\n")
			for person in persons:
				if person.name == buyer_name:
					buyer = person
		elif (elements[0] == "SUBTOTAL"):
			claimed_subtotal = float(elements[2])
			if (abs(claimed_subtotal - counted_subtotal) > 0.01):
				print("WARNING: Claimed subtotal of " + str(claimed_subtotal) + " does not equal counted subtotal of " + str(counted_subtotal))
			buyer = None
			counted_subtotal = 0
		else:
			counted_subtotal += float(elements[0])
			buyer.addItem(Item(elements))	
		
	return persons

if __name__ == "__main__":
	main()

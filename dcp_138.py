'''
	This problem was asked by Google.

	Find the minimum number of coins required to make n cents.

	You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

	For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
'''

def min_coins(value):

	if not value:
		return 0
		
	nr_coins = 0
	aux = value
	
	# go through all the available cent coins
	for coin in [25, 10, 5, 1]:
		# calculate how many coins we can use
		if value >= coin:
			aux = value
			aux //= coin
			nr_coins += aux
			value %= coin
		# number of coins reached
		if not value:
			break
		
	return nr_coins
	
	
assert min_coins(16) == 3
assert min_coins(50) == 2
assert min_coins(1) == 1
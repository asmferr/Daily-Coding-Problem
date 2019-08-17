'''

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def find_numbers(target, list_numbers):
	# create set to store the complement of each number in the list 
	dict_numbers = set()
	
	for num in list_numbers:
		# If the complement is in the list two numbers from the list add up to k
		if target - num in list_numbers:
			return True
		else:
			# Store complement
			dict_numbers.add(target - num)

	return False


assert find_numbers(17, [10, 15, 3, 7]) == True
assert find_numbers(19, [10, 15, 3, 7]) == False


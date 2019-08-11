'''
	This problem was asked by Facebook.

	Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

	For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

	Follow-up: Can you do this in linear time and constant space?
'''

def find_singles_1(list_numbers):
	
	set_numbers = set()
	
	for num in list_numbers:
		if num in set_numbers:
			set_numbers.remove(num)
		else:
			set_numbers.add(num)
			
	
	return set_numbers

find_singles_1([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)
find_singles_1([2, 4, 8, 8, 10, 2, 6, 10]) == (4, 6)


# Follow-up: 
def find_singles_2(list_numbers):

	xored = list_numbers[0]
	# Get the xor of all elements in list_numbers
	for num in list_numbers[1:]:
		xored ^= num

	x, y = 0, 0

	# Get one set bit in the xor2. We get  
	# rightmost set bit in the following  
	# line as it is easy to get
	rightmost_set_bit = (xored & ~(xored - 1))

	# Now divide elements in two sets:  
	# 1 The elements having the corresponding bit as 1.  
	# 2 The elements having the corresponding bit as 0.  
	for num in list_numbers:
		# XOR of first set is finally going to   
		# hold one odd  occurring number x
		if num & rightmost_set_bit:
			x ^= num
		# XOR of second set is finally going  
		# to hold the other odd occurring number y  
		else:
			y ^= num

	return [x, y]
	
find_singles_2([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)
find_singles_2([2, 4, 8, 8, 10, 2, 6, 10]) == (4, 6)

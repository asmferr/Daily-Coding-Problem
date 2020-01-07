'''
This problem was asked by Uber.

Given an list of integers, return a new list such that each element at index i of the new list 
is the product of all the numbers in the original list except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would 
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can’t use division?
'''

def product_except_i(list_numbers):

	n = len(list_numbers)

	# Allocate memory for temporary list left[] and right[] 
	# Left most element of left list is always 1 
	left = [1] + [0] * (n -1)
	# Right most element of right list is always 1 
	right = [0] * (n -1) + [1]

	# Allocate memory for the product list 
	prod = [0] * n 

	# Construct the left list 
	for i in range(1, n): 
		left[i] = list_numbers[i - 1] * left[i - 1] 
	print(left)

	# Construct the right list 
	for j in range(n-2, -1, -1): 
		right[j] = list_numbers[j + 1] * right[j + 1] 
	print(right)

	# Construct the product list using left[] and right[] 
	for i in range(n): 
		prod[i] = left[i] * right[i] 

	return prod
  

assert product_except_i([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_except_i([3, 2, 1]) == [2, 3, 6]

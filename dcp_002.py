'''
This problem was asked by Uber.

Given an list of integers, return a new list such that each element at index i of the new list 
is the product of all the numbers in the original list except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would 
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can’t use division?
'''

'''
Time complexity: O(n) + O(n) = O(n) because we are iterating over the list two times
Space complexity: O(n) because we are creating a new list 
'''
def product_except_i(list_numbers):
    	# neutral element of multiplication
	product = 1

    	# iterate over all elements of the original list and multiply them
	for i in range(0, len(list_numbers)):
		product *= original_list[i]

    	# create new list to store the final result
	new_list = []
	
	# itarate over all the elements of the new list as set the value at position i
	for i in range(0, len(list_numbers)):
		new_list.append(product//list_numbers[i])

	return new_list


'''
Time complexity: O(n-1) + O(n-1) + O(n) = O(n) because we are iterating over the list three times
Space complexity: O(n) because we are creating a new list 
'''
def product_except_i(list_numbers):

	n = len(list_numbers)

	# Allocate memory for temporary list left[] and right[] 
	# Left most element of left list is always 1 
	left = [1] + [0] * (n -1)
	
	# Right most element of right list is always 1 
	right = [0] * (n -1) + [1]
	
	# product list to store the final result
	product = []

	# Construct the left list 
	for i in range(1, n): 
		left[i] = list_numbers[i - 1] * left[i - 1] 

	# Construct the right list 
	for i in range(n-2, -1, -1): 
		right[i] = list_numbers[i + 1] * right[i + 1] 

	# Construct the product list using left[] and right[] 
	for i in range(n): 
		product.append(left[i] * right[i])

	return product
  

assert product_except_i([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_except_i([3, 2, 1]) == [2, 3, 6]

'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''


def largest_sum(l):

	previous, largest = 0, 0
	for val in l:
		previous, largest = largest, max(largest, previous + val)
	
	return largest
	
	
assert largest_sum([5, 1, 1, 5]) == 10
assert largest_sum([2, 4, 6, 8]) == 12
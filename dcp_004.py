'''
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

'''
Approach 1
Use hashing. We can build a hash table of all positive elements in the given array. 
Once the hash table is built. We can look in the hash table for all positive integers, starting from 1. 
As soon as we find a number which is not there in hash table, we return it. 
This approach may take O(n) time on average and it requires O(n) extra space.
'''


def find_smallest(l):
	
	set_l = set()
	# save all positeve integer in the list in a set
	for num in l:
		if l > 0 and l not in set_l:
			set_l.add(l)
	# find smalest integer missing in the list
	for i in range(len(set_l)):
		if i not in set_l:
			return i
	# there is no integer missing in the list so we return next integer
	return len(set_l) + 1
	
	
'''
Approach 2
A O(n) time and O(1) extra space solution:
The idea is similar. We use array elements as index. 
To mark presence of an element x, we change the value at the index x to negative. 
But this approach doesn’t work if there are non-positive (-ve and 0) numbers. 
So we segregate positive from negative numbers as first step and then apply the approach.

Following is the two step algorithm.
1) Segregate positive numbers from others i.e., move all non-positive numbers to left side. In the following code, segregate() function does this part.
2) Now we can ignore non-positive elements and consider only the part of array which contains all positive elements. 
We traverse the array containing all positive numbers and to mark presence of an element x, we change the sign of value at index x to negative. 
We traverse the array again and print the first index which has positive value. 
'''


def find_smallest_2(l):
	j = 0
	for i in range(len(l)):
		if l[i] <= 0:
			# swap elements
			l[i], l[j] = l[j], l[i]
			j += 1
	# consider only the positive integers
	l = l[j:]
	
	# mark l[i] as visited by making it negative 
	for i in range(0, len(l)):
		x = abs(l[i])
		if i - 1 < len(l) and l[i-1] > 0 :
			l[x-1] = -l[x-1]

	# find smalest positive missing
	for i in range(len(l)):
		if l[i] > 0:
			return i + 1
	return i + 1
	
assert find_smallest_2([1, 2, 3, -4, 3, -10, 0]) == 4
assert find_smallest_2([1, 3, -4, 3, -3, 5]) == 2
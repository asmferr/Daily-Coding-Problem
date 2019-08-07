'''
	This question was asked by Riot Games.

	Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

	record(timestamp): records a hit that happened at timestamp
	total(): returns the total number of hits recorded
	range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
	Follow-up: What if our system has limited memory?
'''

class HitCounter():

	def __init__(self):
		self.start_timestamp = None
		self.end_timestamp = None
		self.hits_list = []
		
	def record(self, timestamp):
		# store the first hit
		if not self.start_timestamp:
			self.start_timestamp = timestamp
			
		#add hit to the list and update end_timestamp variable
		self.hits_list.append(timestamp)
		self.end_timestamp = timestamp
		
	def total(self):
		# return size of the list with all the hits
		return len(self.hits_list)
	
	def range(self, lower, upper):
		# get the position of the element 
		start_pos = bisect.bisect_left(self.hits_list, lower)
		end_pos = bisect.bisect_right(self.hits_list, upper)
		return self.hits_list[start_pos:end_pos]
			
	
Follow-up:
	
	
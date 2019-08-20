'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
'''

class Node():

	def __init__(self, val):
		self.val = val
		self.next = None
		self.right = None

		
def serialize(root):
	if not root:
		return None
	# list to store all the values from the tree
	s = []
	
	def serializer(root):
		# child node
		if not node:
			s.append(None)
	
		s.appendstr(str(root.val))
		serialize(root.left)
		serialize(root.right)
	serializer(root)
	return ','.join(s)
	

def deserialize(s):
	# get all the values from the string
	nodes = iter(s.split(','))
	
	def deserializer():
		val = next(node)
		# child node
		if not val:
			return None
		node = Node(int(val))
		node.left = deserializer()
		node.right = deserializer()
		return node
	return deserializer()
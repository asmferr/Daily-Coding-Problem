'''
	This question was asked by Apple.

	Given a binary tree, find a minimum path sum from root to a leaf.

	For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

	  10
	 /  \
	5    5
	 \     \
	   2    1
		   /
		 -1
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

def minimum_path(root):

		if not root:
			return
	
		min_path = []  # store the min path 
		cur_path = []  # strore the current paht
		min_count = float('inf')  # store minimum count 
		cur_count = 0  #stor the current count
		
		# return minimum path from root to leaf founded durind the tree transversal
		return dfs(root, min_path, min_count, cur_path, cur_count)
		
		
def dfs(node, min_path, min_count, cur_path, cur_count):
	
	# add node the the current path and sum it to the current count
	cur_path.append(node.val)
	cur_count += node.val
	
	# if we reach a leaf we update minimum variables if new values founded
	if not node.left and not node.right:
		if cur_count < min_count:
			min_count = cur_count
			min_path = cur_path[:]

			
	# transverse the tree 
	if node.left:
		min_path = dfs(node.left, min_path, min_count, cur_path, cur_count)
	if node.right:
		min_path = dfs(node.right, min_path, min_count, cur_path, cur_count)
	# pop last node added to the list
	cur_path.pop()
	
	return min_path

a = Node(10)
b = Node(5)
c = Node(5)
a.left = b
a.right = c
d = Node(2)
b.right = d
e = Node(1)
c.right = e
f = Node(-1)
e.left = f


path = minimum_path(a)
print("Min path: ", path)
	
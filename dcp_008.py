'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''
     
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def count_unival(root):
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	if not root.left and root.data == root.right.data:
		return 1 + count_unival(root.right)
	if not root.right and root.data == root.left.data:
		return 1 + count_unival(root.left)
		
	if root.data == root.left.data and root.data == root.right.data:
		current_node = 1
	else:
		current_node = 0
	
	child_node = count_unival(root.left) + count_unival(root.right)
	
	
	return current_node + child_node
	
node_a = Node('1')
node_b = Node('1')
node_c = Node('0')
node_d = Node('1')
node_e = Node('0')
node_f = Node('1')
node_g = Node('1')
node_a.left = node_b
node_a.right = node_c
node_c.left = node_d
node_c.right = node_e
node_d.left = node_f
node_d.right = node_g

assert count_unival(None) == 0
assert count_unival(node_a) == 5
assert count_unival(node_c) == 4
assert count_unival(node_g) == 1
assert count_unival(node_d) == 3
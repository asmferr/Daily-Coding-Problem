'''

	This problem was asked by Amazon.

	Given a node in a binary tree, return the next bigger element, also known as the inorder successor. 
	(NOTE: I'm assuming this is a binary search tree, because otherwise, the problem makes no sense at all)

	For example, the inorder successor of 22 is 30.

	   10
	  /  \
	 5    30
		 /  \
	   22    35
	You can assume each node has a parent pointer.

'''
	
	
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, val): 
        self.data = val  
        self.left = None
        self.right = None
  
def in_order_successor(root, n): 

    # Step 1 of the above algorithm 
	if n.right: 
		return min_value(n.right) 
  
    # Step 2 of the above algorithm 
	p = n.parent 
	while(p is not None): 
		if n != p.right : 
			break 
		n = p  
		p = p.parent 
	return p 
  

def min_value(node): 
	'''
	Given a non-empty binary search tree, return the  
	minimum data value found in that tree. Note that the 
	entire tree doesn't need to be searched 
	'''
	current = node 
  
    # loop down to find the leftmost leaf 
	while(current is not None): 
		if current.left is None: 
			break
		current = current.left 
  
	return current 
  
def insert( node, data): 
  
    # 1) If tree is empty then return a new singly node 
	if node is None: 
		return Node(data) 
	else: 
         
        # 2) Otherwise, recur down the tree 
		if data <= node.data: 
			temp = insert(node.left, data) 
			node.left = temp  
			temp.parent = node 
		else: 
			temp = insert(node.right, data) 
			node.right = temp  
			temp.parent = node 
          
		return node 
  
  
  

root  = None
  
# Creating the tree given in the above diagram  
root = insert(root, 20) 
root = insert(root, 8); 
root = insert(root, 22); 
root = insert(root, 4); 
root = insert(root, 12); 
root = insert(root, 10);   
root = insert(root, 14);     
temp = root.left.right.right  
  
succ = in_order_successor( root, temp) 
if succ is not None: 
    print("Inorder Successor of {} is {}".format(temp.data , succ.data)) 
else: 
    print("Inorder Successor doesn't exist")
  
	

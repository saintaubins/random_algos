# Python program to check if a binary tree is bst or not 

INT_MAX = 10
INT_MIN = -10

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


# Returns true if the given tree is a binary search tree 
# (efficient version) 
def isBST(node): 
	return (isBSTUtil(node, INT_MIN, INT_MAX)) 

# Retusn true if the given tree is a BST and its values 
# >= min and <= max 
def isBSTUtil(node, mini, maxi): 
	
	# An empty tree is BST 
	if node is None: 
		return True

	# False if this node violates min/max constraint 
	if node.data < mini or node.data > maxi: 
		return False

	# Otherwise check the subtrees recursively 
	# tightening the min or max constraint 
	return (isBSTUtil(node.left, mini, node.data -1) and
		isBSTUtil(node.right, node.data+1, maxi)) 

# Driver program to test above function 
root = Node(5) 
root.left = Node(3) 
root.right = Node(6) 
root.left.left = Node(2) 
root.left.right = Node(4) 

if (isBST(root)): 
	print("Is BST")
else: 
	print("Not a BST")

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

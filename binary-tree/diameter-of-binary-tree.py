class Node:
     
	# Constructor to create a new Node
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

class Solution:
    
    def diameterOfTree(self, root, res):
        if root == None:
            return 0
        
        ldiameter = self.diameterOfTree(root.left, res)
        rdiameter = self.diameterOfTree(root.right, res)
        
        temp = 1 + max(ldiameter, rdiameter)
        res[0] = max(res[0], 1 + ldiameter + rdiameter)
        
        return temp
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        res = [0]
        self.diameterOfTree(root, res)
        return res[0]

# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
"""
Constructed binary tree is
			1
		  /   \
		2      3
	  /  \
	4     5
"""
 
# Function Call
obj = Solution()
print(obj.diameter(root))
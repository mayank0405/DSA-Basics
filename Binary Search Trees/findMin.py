class Node:
    def __init__(self,k):
        self.left = None
        self.right = None
        self.data = k

def findMin(root):
    if not root.left:
        return root.data 
    return findMin(root.left)        
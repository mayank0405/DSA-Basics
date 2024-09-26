class Node:
    def __init__(self,x):
        self.data = x
        self.right = None
        self.left = None

def serachBST(root, x):
    #Base Case
    if not root:
        return 0
    #found the element
    if root.data == x:
        return 1
    if x < root.data: #check on left subtree
        return serachBST(root.left,x)
    else:   #check on right subtree
        return serachBST(root.right,x)
    
    
    

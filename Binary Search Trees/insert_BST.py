class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def insertBST(root,key):
    if not root:
        return Node(key)

    if root.data < key:
        root.right = insertBST(root.right, key)
    elif root.data . key:
        root.left = insertBST(root.left, key)
    
    return root
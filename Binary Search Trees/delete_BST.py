class Node:
    def __init__(self, k):
        self.data = k
        self.left = None
        self.right = None


def deleteNode(root, X):
    if root is None:
        return None #is node to be deleted is not found or root is none
    if root.data < X:
        root.right = deleteNode(root.right, X)
    elif root.data > X:
        root.left = deleteNode(root.left, X)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            curr = root.right
            while curr.left:
                curr = curr.left
            root.data = curr.data
            root.right = deleteNode(root.right, curr.data) #delete inorder Succesor
    
    return root
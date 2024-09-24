class Node:
    def __init__(self,x) -> None:
        self.right = None
        self.left = None
        self.data = x

def preorder(root):
    res = []
    def func(root):
        if not root:    #base case when root is None or when we reach leaf node
            return
        res.append(root.data)         
        func(root.left)
        func(root.right)
    
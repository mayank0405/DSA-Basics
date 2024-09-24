class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

    
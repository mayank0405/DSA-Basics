class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end = ' ')

    
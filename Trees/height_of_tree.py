class Node:
    def __init__(self, k) -> None:
        self.data = k
        self.left = None
        self.right = None

def height(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)



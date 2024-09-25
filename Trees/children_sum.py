class Node:
    def __init__(self,x) -> None:
        self.left = None
        self.right= None
        self.data = x

def children_sum(root):
    if not root:
        return 1
    if not root.left and not root.right:
        return 1
    left_val = root.left.data if root.left else 0
    right_val = root.right.data if root.right else 0
    root_val = root.data
    if left_val != right_val:
        return 0
    return children_sum(root.left) and children_sum(root.right)



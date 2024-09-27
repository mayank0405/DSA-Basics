class Node:
    def __init__(self, k):
        self.data = k
        self.left = None
        self.right = None


def findCeil(root,x):
    ans = -1
    def func(root,x):
        nonlocal ans
        if not root:
            return -1
        if root.data < x:
            return func(root.right,x)
        else:
            ans = root.data
            return func(root.left, x)
    func(root,x)
    return ans
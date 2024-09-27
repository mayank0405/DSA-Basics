class Node:
    def __init__(self,k):
        self.data = k
        self.left = None
        self.right = None


def findFloor(root, x):
    ans = -1
    def func(root,x):
        nonlocal ans
        if not root:
            return -1
        if root.data > x:
            return func(root.left)
        else:
            ans = root.data
            return func(root.right)
    func(root,x)
    return ans
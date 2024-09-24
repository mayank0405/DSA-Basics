class Node:
    def __init__(self, k):
        self.data = k
        self.left = None
        self.right=  None

from collections import deque
def levelOrder(root):
    if not root:
        return -1
    dq = deque()
    res = []
    dq.append(root)
    while dq:
        node = dq.popleft()
        res.append(node.data)
        if node.left:
            dq.append(node.left)
        if node.right:
            dq.append(root.right)
    return res



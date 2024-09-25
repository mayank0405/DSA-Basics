class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


def identicalTrees(root1, root2):
    if not root1 and not root2:
        return 1
    if root1 is not None and root2 is not None:
        return (root1.data == root2.data and (identicalTrees(root1.left, root2.left)) and (identicalTrees(root1.right, root2.right)))
    return 0
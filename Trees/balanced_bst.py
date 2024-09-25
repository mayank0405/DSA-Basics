class Node:
    def __init__(self,x):
        self.data = x
        self.right = None
        self.left = None

'''
Since ans is being modified inside the height function, 
you need to declare it as nonlocal so that Python knows you're referring to the ans 
variable from the enclosing scope.'''

def balanced_bst(root):
    ans = True
    def height(root):
        nonlocal ans
        if not root:
            return 0
        left_height = height(root.left)
        right_height = height(root.right)
        diff = abs(right_height - left_height)
        if diff > 1:
            ans = False
            return 0
        return 1 + max(left_height, right_height)
    height(root)
    return ans
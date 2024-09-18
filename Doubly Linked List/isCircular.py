class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None

def isCircular(head):
    if not head:
        return False
    if head.next == head:
        return True
    curr = head
    while curr:
        curr = curr.next
        if curr == head:
            return True
    return False        
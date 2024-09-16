class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def checkCircular(head):
    if not head:
        return False
    if head.next == head:
        return True
    curr = head
    curr = curr.next
    while curr.next != head:
        curr = curr.next
    if curr.next == head:
        return True
    else:
        return False
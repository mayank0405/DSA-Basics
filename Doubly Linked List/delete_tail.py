class Node:
    def __init__(self,k):
        self.prev = None
        self.next = None
        self.data = k

def deleteTail(head):
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head
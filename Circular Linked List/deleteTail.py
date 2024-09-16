class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def deleteTail(head):
    if not head:
        return head
    if head.next is None:
        return None
    curr = head
    curr = curr.next
    while curr.next.next != head:
        curr = curr.next
    curr.next = head
    return head
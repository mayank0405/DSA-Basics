class LinkedList:
    def __init__(self, k):
        self.data = k
        self.next = None
        self.head = None

def reverseLL(head):
    if not head or not head.next:
        return head
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev        
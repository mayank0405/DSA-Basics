class LinkedList:
    def __init__(self,k):
        self.next = k
        self.head = None
        self.next = None

def reverseLL(head):
    if head is None or head.next is None:
        return head
    new_head = reverseLL(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head        
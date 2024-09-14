class LinkedList:
    def __init__(self, k):
        self.data = k
        self.next = None
        self.head = None

def deleteHead(head):
    if not head or not head.next:
        return head
    curr  = head
    while curr.next.next: # we have to go to the second last node
        curr = curr.next
    curr.next = None
    return head
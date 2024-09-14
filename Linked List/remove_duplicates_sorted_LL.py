class LinkedList:
    def __init__(self, k):
        self.data = k
        self.next = None
        self.head = None

def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        curr = curr.next
    return head        
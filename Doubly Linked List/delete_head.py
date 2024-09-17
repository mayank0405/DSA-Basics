class Node:
    def __init__(self,k):
        self.data = k
        self.prev = None
        self.next = None

def deleteHead(head):
    if not head:
        return head
    if head.next == None:
        return None
    head = head.next
    head.prev = None
    return head        
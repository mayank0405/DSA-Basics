class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None

def insertInTail(head,data):
    new_tail = Node(data)
    if not head:
        return new_tail
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_tail
    new_tail.prev = curr
    return head
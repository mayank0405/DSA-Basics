class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None

def reverseDLL(self, head):
        if not head:
            return head
        if head.next == None:
            return head
        curr = head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            head = curr
            curr = curr.prev
        return head        
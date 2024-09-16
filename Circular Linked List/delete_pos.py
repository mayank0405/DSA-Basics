class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def delete(head, pos):
    if not head:
        return head
    if head == head.next and pos == 1:
        return None
    if pos == 1:
        head.data = head.next.data
        head.next = head.next.next
    else:
        for i in range(pos-2):
            curr = curr.next
        if curr.next.next == head:
            curr.next = head
        else:
            curr.next = curr.next.next
    return head
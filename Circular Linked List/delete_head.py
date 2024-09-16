class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

#Method - 1
def deleteHead1(head):
    if not head:
        return head
    if head.next == head:
        return None
    curr = head
    curr = curr.next
    while curr.next != head:
        curr = curr.next
    curr.next = head.next
    head = head.next  
    return head

#Method - 2
def deleteHead2(head):
    if not head:
        return head
    if head == head.next:
        return None
    head.data = head.next.data
    head.next = head.next.next
    return head      
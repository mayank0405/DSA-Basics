class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def insertTail(head, val):
    new_node = Node(val)
    if not head:
        new_node.next = new_node
        return new_node
    if head.next == head:
        head.next = new_node
        new_node.next = head
        return head
    curr = head
    curr = curr.next
    while curr.next != head:
        curr = curr.next
    temp = curr.next
    curr.next = new_node 
    new_node.next = temp
    return head
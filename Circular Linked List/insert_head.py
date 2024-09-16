class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def insertHead(head, val):
    new_node = Node(val)
    if not head:
        new_node.next = new_node
        return new_node
    curr = head
    curr = curr.next
    while curr.next != head:
        curr = curr.next
    curr.next = new_node
    new_node.next = head
    return new_node
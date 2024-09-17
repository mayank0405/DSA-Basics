class Node:
    def __init__(self, k):
        self.data = k
        self.next = None
        self.prev = None

def sortedInsert(head, x):
    new_node = Node(x)
    if not head:
        return new_node
    if x < head.data:
        new_node.next = head
        head.prev = new_node
        return new_node
    curr = head
    while curr.next and curr.next.data < x:
        curr = curr.next
    nxt = curr.next
    curr.next = new_node
    new_node.prev = curr
    new_node.next = nxt
    return head        
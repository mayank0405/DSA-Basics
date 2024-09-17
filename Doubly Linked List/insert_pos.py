class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None

def addNode(head, p, data):
    new_node = Node(data)
    if not head:
        return new_node
    if head.next == None and p == 1:
        head.next = new_node
        new_node.prev = head
        return head
    curr = head
    for i in range(p):
        curr = curr.next
    nxt = curr.next
    curr.next = new_node
    new_node.prev = curr
    new_node.next = nxt
    return head        
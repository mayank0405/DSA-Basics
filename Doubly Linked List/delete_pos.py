class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None

def deletePos(head, pos):
    if not head:
        return None
    if pos == 1:
        head = head.next
        if head: #if DLL containts more than one node.
            head.prev = None
        return head
    curr = head
    for _ in range(pos-2):
        if curr is None or curr.next is None: #x is out of bounds
            return head
        curr = curr.next
    node_to_delete = curr.next
    if node_to_delete is None:
        return head
    curr.next = node_to_delete.next
    if node_to_delete.next: # if element after the node to delete is containing more elements
        node_to_delete.next.prev = curr
    return head
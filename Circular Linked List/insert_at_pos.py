class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def insertPos(head, val,pos):
    new_node = Node(val)
    if not head:
        new_node.next = new_node
        return new_node
    if pos == 1 and head.next == head:
        new_node.next = head
        head.next = new_node
        head.data, new_node.data = new_node.data, head.data
    else:
        curr = head
        for i in range(pos-1):
            curr = curr.next
            if curr == head:
                return
        new_node.next = curr.next
        curr.next = new_node
        return head
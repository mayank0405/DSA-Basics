class LinkedList:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.head = None

def insertSorted(head,x):
    new_node = LinkedList(x)
    if head is not None:
        return new_node 
    if head.data < x:
        new_node.next = head
        return new_node
    curr = head
    while curr.next and curr.next.data < x:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head       
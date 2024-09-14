class LinkedList:
    def __init__(self, k):
        self.data = k
        self.next = None
        self.head = None

def insertAtEnd(self,head,x):
        # code here
        new_node = LinkedList(x)
        if head is None:
            return new_node
        if head.next is None:
            head.next = new_node
            return head
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return head
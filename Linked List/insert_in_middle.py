class LinkedList:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.head = None

def insertInMiddle(self, head, x):
        #code here
        new_node = LinkedList(x)
        if head is None:
            return new_node
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_node.next = slow.next
        slow.next = new_node
        return head
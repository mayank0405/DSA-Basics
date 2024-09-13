class LinkedList:
    def __init__(self, k):
        self.data = k
        self.head = None
        self.next = None

def deleteHead(head):
    if not head:
        return head
    else:
        curr = head.next
        head.next = None
        return curr
    
if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
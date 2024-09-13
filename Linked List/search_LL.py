class LinkedList:
    def __init__(self, k):
        self.data = k
        self.head = None
        self.next = None

def searchLL(head,x):
    if not head:
        return False
    curr = head
    while curr:
        if curr.data == x:
            return True
        curr = curr.next
    return False

if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    ans = searchLL(head,10)
    print(ans)


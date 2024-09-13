class LinkedList:
    def __init__(self, k):
        self.data = k
        self.head = None
        self.next = None

def getCount(head):
    count = 0
    if not head:
        return count
    curr = head
    while curr:
        curr = curr.next
        count += 1
    return count

if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    ans = getCount(head)
    print(f'Number of nodes are: {ans}')
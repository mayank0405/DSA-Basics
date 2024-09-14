class LinkedList:
    def __init__(self, k):
        self.next = None
        self.data = k
        self.head = None

def check_sort(head):
    if not head or head.next is None:
        return 1
    inc = True
    dec = True
    curr = head
    while curr.next:
        if curr.data > curr.next.data:
            inc = False
        if curr.data < curr.next.data:
            dec = False

    return 1 if dec or inc else 0        
class LinkedList:
    def __init__(self, k):
        self.head = None
        self.next = None
        self.data = k

def kthElement(head,k):
    if not head or head.next == None:
        return head
    
    fast = head
    for i in range(k):
        if fast == None: #if k goes out of LL
            return -1
        fast = fast.next
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next

    return slow.data

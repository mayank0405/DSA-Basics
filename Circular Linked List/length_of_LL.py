class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def getLength(head):
    if not head:
        return 0
    curr = curr.next
    count = 1
    while curr != head:
        curr = curr.next
        count +=1
    return count
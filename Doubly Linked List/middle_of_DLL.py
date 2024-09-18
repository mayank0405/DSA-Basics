class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None


def middle_of_DLL(head):
    #the DLL is circular in nature.
    if not head:
        return None
    if head.next is None:
        return head
    slow,fast = head,head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data 
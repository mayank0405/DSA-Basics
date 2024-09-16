class Node:
    def __init__(self,k):
        self.data = k
        self.head = None
        self.next = None

def display(head):
    if not head:
        return []
    if head.next == head:
        return [head.data]
    ans = []
    ans.append(head.data)
    curr = head.next
    while curr != head:
        ans.append(curr.data)
        curr =curr.next
    return ans
class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None

def returnDLL(head):
    if not head:
        return []
    ans = []
    curr = head
    while curr:
        ans.append(curr.data)
        curr = curr.next
    return ans         
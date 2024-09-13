class LinkedList:
    def __init__(self, k):
        self.data = k
        self.head = None
        self.next = None

def delete_pos(head, pos):
    if not head:
        return head
    if pos == 1:
        curr = head.next
        head.next = None
        return curr
    for i in range(pos-2):
        curr = curr.next
    if curr == None or curr.next == None:
        return head
    curr.next = curr.next.next
    return head

if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
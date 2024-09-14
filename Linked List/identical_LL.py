class LinkedList:
    def __init__(self, k):
        self.data = k
        self.head = None
        self.next = None

def areIdentical(self, head1, head2):
        # Code here
        if head1 is None and head2 is None:
            return True
        if (head1 is None and head2 is not None) or (head1 is not None and head2 is None):
            return False
        curr1 = head1
        curr2 = head2
        while curr1.next and curr2.next:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        if (curr1.next is None and curr2.next is not None) or (curr1.next is not None and curr2.next is None):
            return False
        return True
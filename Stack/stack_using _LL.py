class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node  
            return self.head
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return -1
        popdata = self.head.data
        self.head = self.head.next
        return popdata     
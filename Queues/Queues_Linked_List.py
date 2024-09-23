class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head = self.rear = None
    
    #Function to push an element into the queue.
    def push(self, item):
        new_node = Node(item)
        if self.head == self.rear == None:
            self.head = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.head == self.rear == None:
            return -1
        
        pop_item = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.rear = None
        return pop_item
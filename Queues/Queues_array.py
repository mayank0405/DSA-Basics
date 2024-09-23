#User function Template for python3

class MyQueue:
    def __init__(self):
        self.arr = []
        
    #Function to push an element x in a queue.
    def push(self, x):
         return self.arr.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
         if len(self.arr) == 0:
             return -1
         return self.arr.pop(0)
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if (self.size > 0):
            self.size -= 1
            returnValue = self.storage[0]
            self.storage =self.storage[1:]
            return returnValue
        else:
            return None

    def len(self):
        return self.size
q = Queue()
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q.dequeue()) #100
print(q.len()) #2
print(q.dequeue())#101
print(q.len())#1
print(q.dequeue())#105
print(q.len())#0
print(q.dequeue())
print(q.len())#0
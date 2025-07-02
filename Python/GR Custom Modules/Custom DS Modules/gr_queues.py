
class MyQueue: 

    """
    This implementation of Queues were base on the circular Queue implementation made prior this one.
    This implementation supposed a Queue with a limited capacity
    """

    def __init__(self, size):
        
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1


    def is_empty(self):

        return self.front == -1


    def is_full(self):

        return self.rear == self.size - 1


    def enqueue(self, data):

        if self.is_full():
            return print('Full Queue, Cannot Enqueue')
        
        if self.is_empty():
            self.rear = self.front = 0

        else:
            self.rear += 1
               
        self.queue[self.rear] = data


    def dequeue(self):

        if self.is_empty():
            return print('Empty Queue, Cannot Dequeue')
        
        item = self.queue[self.front]
        
        if self.rear == self.front:
            self.rear = self.front = -1

        else:
            self.rear -= 1

        return item


    def display (self):

        if self.is_empty():
           return print('Empty Queue')
        
        [print(elem, end=' ') for elem in self.queue[:self.rear]]

        print(self.queue[self.rear])




class ListQueue:

    """
    This is a simplyfied version of the Queue implementation based on built-in list datatype
    This implementation supposed a Queue with an unlimited capacity
    """

    def __init__(self):

        self.queue = list()

    
    def is_empty(self):

        return len(self.queue) == 0
    

    def enqueue(self, data):

        self.queue.append(data)
    

    def dequeue(self):

        return self.queue.pop(0)

    
    def display(self):

        if self.is_empty():
           return print('Empty Queue')
        
        [print(elem, end=' ') for elem in self.queue[:-1]]

        print(self.queue[-1])




class MyCircularQueue:

    def __init__(self, size):

        self.size = size
        self.queue = [None] * size
        self.rear = self.front = -1


    def is_empty(self):
        return self.front == -1
    

    def is_full(self):    
        return (self.rear + 1) % self.size == self.front
    

    def enqueue(self, data):

        if self.is_full():
            return print('Queue full. Cannot enqueue')
        

        if self.is_empty():
            
            self.rear = self.front = 0

        else:

            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
            
    
    def dequeue(self):

        if self.is_empty():
            return print('Queue empty. Cannot dequeue')
        
        item = self.queue[self.front]

        if self.rear == self.front:
            self.rear = self.front = -1

        else:
            self.front = (self.front + 1) % self.size

        return item
    

    def display(self):

        if self.is_empty():
            return print('Empty Queue')
        

        idx = self.front

        while idx != self.rear:

            print(self.queue[idx], end=' ')
            idx = (idx + 1) % self.size
        
        print(self.queue[self.rear])




class MyPriorityQueue:

    "This implementation is based on a Z-A prioritization criteria"

    
    def __init__(self):

        self.queue = list()

    
    def is_empty(self):

        return len(self.queue) == 0
    

    def enqueue(self, data, priority):

        self.queue.append((data, priority))
        self.queue.sort(key = lambda x: -x[1])
    

    def dequeue(self):

        return self.queue.pop(0)

    
    def display(self):

        if self.is_empty():
           return print('Empty Queue')
        
        [print(elem, end=' ') for elem in self.queue[:-1]]

        print(self.queue[-1])




class MyDeque:

    def __init__(self):
        self.queue = list()

    
    def is_empty(self):
        return len(self.queue) == 0
    

    def enqueue_right(self, data):
        self.queue.append(data)
    

    def enqueue_left(self, data):
        self.queue.insert(0,data)

    
    def dequeue_right(self):
        return self.queue.pop()

    
    def dequeue_left(self):
        return self.queue.pop(0)
    

    def display(self):

        if self.is_empty():
           return print('Empty Queue')
        
        [print(elem, end=' ') for elem in self.queue[:-1]]

        print(self.queue[-1])


    

























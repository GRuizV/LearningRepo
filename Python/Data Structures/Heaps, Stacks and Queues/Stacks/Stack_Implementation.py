
class Stack:

    def __init__(self):

        self.stack = []


    def is_empty(self):

        if not self.stack:
            return True
        else:
            return False


    def insert(self, data):

        self.stack.append(data)

    
    def pop(self):

        if self.is_empty():
            return
        
        popped = self.stack.pop()
        return popped
    

    def peak(self):

        if self.is_empty():
            return print('Empty Stack')

        return print(self.stack[-1])


    def stack_size(self):

        return len(self.stack)
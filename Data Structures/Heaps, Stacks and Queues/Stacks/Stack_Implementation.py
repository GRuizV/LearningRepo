
class Stack:

    def __init__(self):

        self.stack = []


    def is_empty(self):

        if not self.stack:
            return True
        else:
            return False


    def insert(self, data):

        self.stack = [data] + self.stack

    
    def pop(self):

        self.stack = self.stack[1:]
    

    def peak(self):

        if self.is_empty():
            return print('Empty Stack')

        return print(self.stack[0])


    def stack_size(self):

        return len(self.stack)
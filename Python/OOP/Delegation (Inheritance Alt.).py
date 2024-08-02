
'Delegation'

class Stack:

    def __init__(self, items=None ):

        if items is None:
            self._items = []
        
        else:
            self._items = list(items)

    def push(self, item):
        self._items.append(item)
    
    def pop(self, item):
        return self._items.pop()
    
    def __repr__(self):
        return f"{type(self).__name__}({self._items})"
    


stack = Stack([1,2,3,4])
print(stack)    # Stack([1, 2, 3, 4])

print(dir(stack))

# [...
# 
#   '_items',
#   'pop',
#   'push'
# ...]




'Inheritance'

class Stack(list):

    def push(self,item):
        self.append(item)

    def pop(self):
        return super().pop

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"


stack = Stack([1,2,3,4])
print(stack)    # Stack([1, 2, 3, 4])

print(dir(stack))

# [
#     ...
#     'append',
#     'clear',
#     'copy',
#     'count',
#     'extend',
#     'index',
#     'insert',
#     'pop',
#     'push',
#     'remove',
#     'reverse',
#     'sort'
# ]

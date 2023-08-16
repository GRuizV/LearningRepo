import Stack_Implementation
import random

stack = Stack_Implementation.Stack() 

# input_data = [random.randint(0,30) for _ in range(5)]
input_data = [5, 0, 22, 26, 10]
print(input_data)

[stack.insert(num) for num in input_data]

print(stack.stack)

stack.pop()
stack.pop()

print(stack.stack)

stack.peak()

stack.pop()
stack.peak()

stack.pop()
stack.peak()

stack.pop()
stack.peak()

stack.pop()
stack.peak()

print(stack.stack_size())








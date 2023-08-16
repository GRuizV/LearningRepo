import queue
import random

stack = queue.LifoQueue(maxsize=5)


input_data = [random.randint(0,30) for _ in range(5)]
[stack.put(num) for num in input_data]


print(f'Stack maxsize: {stack.maxsize}')

print(f'Empty Stack: {stack.empty()}')

print(f'Full Stack: {stack.full()}')

print(f'Stack Size: {stack.qsize()}')

print(stack.queue)

item = stack.get()

print(stack.queue, f'removed: {item}')

print(f'Stack Size: {stack.qsize()}')
print()


print(stack.all_tasks_done)
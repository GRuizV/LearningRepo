from collections import deque
from queue import Queue



'Deque from collections'

# my_deque = deque(maxlen = 5)

# [my_deque.append(elem) for elem in  [2, 1, 5, 7, 9]]

# print(my_deque)
# print()

# my_deque.append('X')

# print(my_deque)
# print()

# my_deque.popleft()

# print(my_deque)
# print()


# [print(elem, end=' ') for elem in my_deque]
# print('\n')


# my_deque.rotate(1)

# print(my_deque)
# print()

# my_deque.rotate(-2)

# print(my_deque)
# print()



'Queue from queue module'


my_queue = Queue(maxsize = 5)

[my_queue.put(elem) for elem in  [2, 1, 5, 7, 9]]

print(my_queue.get())

my_queue.put('X')

print(my_queue.empty())

print(my_queue.full())

print(f'size: {my_queue.qsize()}')

print(my_queue.get())

print(f'size: {my_queue.qsize()}')














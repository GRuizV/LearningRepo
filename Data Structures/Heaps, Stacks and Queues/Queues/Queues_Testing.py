import random
import Queues_Implementation


'Circular Queue'

cir_queue = Queues_Implementation.MyCircularQueue(size = 5)

# [cir_queue.enqueue(random.randint(0,5)) for _ in range(5)]
[cir_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# cir_queue.display()
print()


print(f'Queue:', end=' ')
cir_queue.display()
print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
print(f'Queue as att.: {cir_queue.queue}')
print(f'Queue front index: {cir_queue.front}')
print(f'Queue rear index: {cir_queue.rear}')



cir_queue.dequeue()
print()



print(f'Queue:', end=' ')
cir_queue.display()
print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
print(f'Queue as att.: {cir_queue.queue}')
print(f'Queue front index: {cir_queue.front}')
print(f'Queue rear index: {cir_queue.rear}')



cir_queue.enqueue('X')
print()



print(f'Queue:', end=' ')
cir_queue.display()
print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
print(f'Queue as att.: {cir_queue.queue}')
print(f'Queue front index: {cir_queue.front}')
print(f'Queue rear index: {cir_queue.rear}')



cir_queue.enqueue('X')
print()


cir_queue.dequeue()
cir_queue.dequeue()
cir_queue.dequeue()
cir_queue.dequeue()
print()



print(f'Queue:', end=' ')
cir_queue.display()
print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
print(f'Queue as att.: {cir_queue.queue}')
print(f'Queue front index: {cir_queue.front}')
print(f'Queue rear index: {cir_queue.rear}')



cir_queue.dequeue()
print()



print(f'Queue:', end=' ')
cir_queue.display()
print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
print(f'Queue as att.: {cir_queue.queue}')
print(f'Queue front index: {cir_queue.front}')
print(f'Queue rear index: {cir_queue.rear}')



[cir_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
print()



cir_queue.enqueue('X')
print()



print(f'Queue:', end=' ')
cir_queue.display()
print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
print(f'Queue as att.: {cir_queue.queue}')
print(f'Queue front index: {cir_queue.front}')
print(f'Queue rear index: {cir_queue.rear}')

























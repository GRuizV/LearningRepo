import random
import Queues_Implementation


'Regular Queues'

'   Queue based on circular implementation'
# my_queue = Queues_Implementation.MyQueue(size = 5)
# [my_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# my_queue.display()
# print()


# my_queue.enqueue('X')
# print()

# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.enqueue('X')
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')


# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[my_queue.front]}')
# print(f'Queue rear: {my_queue.queue[my_queue.rear]}')
# print(f'Queue as att.: {my_queue.queue}')
# print(f'Queue front index: {my_queue.front}')
# print(f'Queue rear index: {my_queue.rear}')




'   Queue based on circular implementation'

# my_queue = Queues_Implementation.ListQueue()
# [my_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# # my_queue.display()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')


# my_queue.dequeue()
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')


# my_queue.enqueue('X')
# print()


# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')



# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}')
# print(f'Queue rear: {my_queue.queue[-1]}')
# print(f'Queue as att.: {my_queue.queue}')



# my_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# my_queue.display()
# print(f'Queue front: {my_queue.queue[0]}' if not my_queue.is_empty() else None)
# print(f'Queue rear: {my_queue.queue[-1]}' if not my_queue.is_empty() else None)
# print(f'Queue as att.: {my_queue.queue}')





'Circular Queue'

# cir_queue = Queues_Implementation.MyCircularQueue(size = 5)

# # [cir_queue.enqueue(random.randint(0,5)) for _ in range(5)]
# [cir_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# # cir_queue.display()
# print()


# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.enqueue('X')
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.enqueue('X')
# print()


# cir_queue.dequeue()
# cir_queue.dequeue()
# cir_queue.dequeue()
# cir_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# cir_queue.dequeue()
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')



# [cir_queue.enqueue(x) for x in [1, 8, 3, 5, 2]]
# print()



# cir_queue.enqueue('X')
# print()



# print(f'Queue:', end=' ')
# cir_queue.display()
# print(f'Queue front: {cir_queue.queue[cir_queue.front]}')
# print(f'Queue rear: {cir_queue.queue[cir_queue.rear]}')
# print(f'Queue as att.: {cir_queue.queue}')
# print(f'Queue front index: {cir_queue.front}')
# print(f'Queue rear index: {cir_queue.rear}')

























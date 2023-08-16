from Heap_Implementation import MaxHeap, MinHeap
import random
import math


'MaxHeap Testing'
new_heap = MaxHeap()

[new_heap.insert(random.randint(0,11)) for _ in range(0,9)]
# [new_heap.insert(i) for i in [10, 10, 9, 5, 3, 1, 6, 0]]

new_heap.display()

print()

new_heap.display_heap()

print()
# print(new_heap.find_min())
# print()

# new_heap.delete(8)
# new_heap.display()
# print()
# new_heap.display_heap()





'MinHeap Testing'

new_heap = MinHeap()

# [new_heap.insert(random.randint(0,11)) for _ in range(0,9)]
# [5, 11, 6, 2, 3, 11, 6, 4, 2]
[new_heap.insert(i) for i in [5, 11, 6, 2, 3, 11, 6, 4, 2]]

new_heap.display()

print()

new_heap.display_heap()
# print()


# heap_min = new_heap.extract_min()

# new_heap.display()

# print()

# new_heap.display_heap()
# print()

# print(heap_min)


# print(new_heap.find_max())


# new_heap.delete(4)

# new_heap.display()
# print()
# new_heap.display_heap()


import heapq
from math import log
import random


def display_heap(heap):
    
    first = lambda h: 2**h - 1      # H stands for level height
    last = lambda h: first(h + 1)
    level = lambda heap, h: heap[first(h):last(h)]
    prepare = lambda e, field: str(e).center(field)

    width = max(len(str(e)) for e in heap)

    height = int(log(len(heap), 2)) + 1    
    gap = ' ' * width

    for h in range(height):
        below = 2 ** (height - h - 1)
        field = (2 * below - 1) * width
        print(gap.join(prepare(e, field) for e in level(heap, h)))



# l = [random.randint(0,11) for x in range(15)]
l = [9, 8, 11, 0, 1, 8, 3, 11, 6, 2, 0, 1, 4, 3, 0]
print(f'Base list: {l}')


heapq.heapify(l)    # This method modifies the base data
print(f'Resulting heap: {l}')


display_heap(l)
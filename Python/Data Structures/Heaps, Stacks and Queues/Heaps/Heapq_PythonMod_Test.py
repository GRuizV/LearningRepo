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
l = [9, 8, 11, 4, 1, 8, 3, 11, 6, 2, 7, 1, 4, 3]
print(f'Base list: {l}')


heapq.heapify(l)    # This method modifies the base data
print(f'Resulting heap: {l}')
print()


# display_heap(l)
# print()


heapq.heappush(l,0)
# display_heap(l)
# print()


heapq.heappop(l)
# display_heap(l)
# print()

heapq.heappushpop(l,13)
display_heap(l)
print()

print(l)
print()


largest = heapq.nlargest(3,l)
print(largest)
print()


smallest = heapq.nsmallest(3,l)
print(smallest)
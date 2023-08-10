from Heap_Implementation import MaxHeap
import random

new_heap = MaxHeap()

[new_heap.insert(random.randint(0,11)) for _ in range(0,9)]
# [new_heap.insert(i) for i in [10, 10, 9, 5, 3, 1, 6, 0]]

new_heap.display()

print()

new_heap.display_heap()

# print()
# print(new_heap.find_min())
print()

new_heap.delete(0)
new_heap.display()
print()

new_heap.display_heap()





# Heap display func under dev.

# def display_heap(heap):
       
#     def get_level(index):
#         return (index.bit_length() - 1) if index > 0 else 0

#     def print_spaces(count):
#         print(" " * count, end="")

#     def print_branches(levels, current_level, index):
#         if current_level >= levels:
#             return

#         elements_in_level = 2 ** current_level
#         spaces_between_elements = 2 ** (levels - current_level) - 1

#         print_spaces(spaces_between_elements)

#         for i in range(elements_in_level):
#             current_index = (2 ** current_level - 1) + i
#             if current_index < len(heap):
#                 print(f"{heap[current_index]:>4}", end="")
#             else:
#                 break

#             if i < elements_in_level - 1:
#                 print_spaces(spaces_between_elements * 2)

#         print()

#         next_level = current_level + 1
#         for i in range(elements_in_level):
#             current_index = (2 ** current_level - 1) + i
#             left_child_index = current_index * 2 + 1
#             right_child_index = current_index * 2 + 2

#             if left_child_index < len(heap) and get_level(left_child_index) == next_level:
#                 print_spaces(spaces_between_elements)
#                 print_branches(levels, next_level, left_child_index)

#             if right_child_index < len(heap) and get_level(right_child_index) == next_level:
#                 print_spaces(spaces_between_elements)
#                 print_branches(levels, next_level, right_child_index)

#     height = get_level(len(heap) - 1) + 1
#     print_branches(height, 0, 0)














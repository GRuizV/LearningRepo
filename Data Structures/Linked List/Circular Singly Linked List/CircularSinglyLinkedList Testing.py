from CircularSinglyLinkedList import *

new_list = CircularSinglyLinkedList()


new_list.append('Beth')

new_list.append('George')

new_list.append('Kathy')

new_list.append('Beth')

new_list.append('Sam')

new_list.insert_after('Joey', 'Sam')

new_list.prepend('Tom')

new_list.reverse()

# new_list.print_list()
# print()


list_to_extend = CircularSinglyLinkedList()
[list_to_extend.append(x) for x in 'XYZ']

list_to_extend_2 = CircularSinglyLinkedList()
[list_to_extend_2.append(x) for x in 'ABC']

list_to_extend_2.extend(list_to_extend)

# list_to_extend_2.print_list()
# print()


# a = list_to_extend_2.pop(1)

# list_to_extend_2.print_list()

# list_to_extend_2.print_nodes()

# print(a.data)

# list_to_extend_2.clear()
# list_to_extend_2.print_list()





# list_sort = CircularSinglyLinkedList()

# [list_sort.append(x) for x in 'BCA']

# list_sort.print_list()

# list_sort.bubble_sort()
# print()

# list_sort.print_list()
# print()

# list_sort.print_nodes()


new_list = CircularSinglyLinkedList()

new_list.append('A')

new_list.delete('A')

new_list.print_list()



_ = '-----------------------------------------------------------------------'


_ = "What's next?"

'''
3. Finish implementing Bubble sort for Cirular Singly
4. Move on to Circular Doubly
'''


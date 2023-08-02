from DoublyLinkedList import *

new_linked_list = DoublyLinkedList()


new_linked_list.append('Beth')
new_linked_list.append('George')
new_linked_list.prepend('Jimmy')
new_linked_list.append('Beth')
new_linked_list.append('Kathy')
new_linked_list.append('Beth')
new_linked_list.append('Ben')
new_linked_list.prepend('Mike')
new_linked_list.insert_after('Joe', 'George')

# new_linked_list.search('Zeke')
# new_linked_list.search('Beth')
# new_linked_list.search('George')

# new_linked_list.delete('Ben')

# new_linked_list.print_list()

new_linked_list.reverse()

# new_linked_list.print_list()


# test_list = DoublyLinkedList()

# test_list.append('A')
# test_list.append('B')
# test_list.append('C')
# test_list.append('D')


# new_linked_list.extend(test_list)

# new_linked_list.print_list()

# a = new_linked_list.return_node(-1)

# print(a.next)



# popped_node = new_linked_list.pop()

# new_linked_list.print_list()

# print(popped_node.data)



# new_linked_list.bubble_sort()

# new_linked_list.print_list()

# new_linked_list.print_nodes()

# new_linked_list.delete('Ben')
# new_linked_list.print_list()
# print()

# new_linked_list.print_nodes()



new_list = DoublyLinkedList()

[new_list.append(x) for x in 'BCA']

new_list.print_list()
print()

new_list.bubble_sort()

new_list.print_list()
print()

new_list.print_nodes()







_ = '-----------------------------------------------------------------------'







_ = 'DOUBLY LINKED LIST EXERCISE'

'''
9. Write a Python program to create a doubly linked list and print nodes from current position to first node.
Click me to see the sample solution
'''


# new_linked_list.print_list()
# print()


# def print_from(index, linked_list = DoublyLinkedList()):

#     index = linked_list._index_handler(index)

#     node = linked_list.return_node(index)

#     while node is not None:

#         print(node.data, end = ' ')

#         node = node.prev


# print_from(-5, new_linked_list)








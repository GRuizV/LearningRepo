from DoublyCircularLinkedList import *



new_list = DoublyCircularLinkedList()
[new_list.append(x) for x in 'ABCVA']

new_list.prepend('Z')

new_list.insert_after('Y', 'B')

# new_list.search('B')

# new_list.clear_list()
# new_list.print_list()

new_list.delete('C')

# new_list.print_list()
# new_list.print_nodes()



new_list = DoublyCircularLinkedList()
[new_list.append(x) for x in 'FED']


new_list.print_list()

new_list.bubble_sort()

new_list.print_list()

new_list.print_nodes()
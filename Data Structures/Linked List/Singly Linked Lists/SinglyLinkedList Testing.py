from SinglyLinkedList import *


# new_linked_list = SinglyLinkedList()

# new_linked_list.head = Node('Albert')

# new_linked_list.append('Beth')

# new_linked_list.append('George')

# new_linked_list.prepend('Jimmy')

# new_linked_list.append('Beth')

# new_linked_list.append('Kathy')

# new_linked_list.append('Beth')

# new_linked_list.append('Ben')

# new_linked_list.insert_after('Jerome', 'Ben')

# new_linked_list.prepend('Kevin')

# new_linked_list.append('John')

# new_linked_list.delete('Kevin')

# new_linked_list.insert_after('Claude', 'Kathy')

# new_linked_list.delete('John')

# new_linked_list.print_list()
# print()


# new_linked_list.bubble_sort_list()


# new_linked_list.print_list()
# print()


# new_linked_list.reverse_list()


# new_linked_list.print_list()


# new_list = SinglyLinkedList()


# [new_list.append(x) for x in 'CDBEA']


# new_list.print_list()

# new_list.bubble_sort()

# new_list.print_list()





_ = 'Interview Preparation Kit - Removing dupliates from a Linked List'


# new_list = SinglyLinkedList()


# #[3,9,9,11,11,11,11,89,89,100,100,101,102,103,108,200,250,250,250,250]
# #[3,9,9,9,11,11,11,250,250,250,250]

# [new_list.append(x) for x in [3,9,3,11,250,3]]

# new_list.print_list()


# def remove_dupl(llist = SinglyLinkedList()):

#     current = llist.head
   
#     while current is not None:

#         runner = current

#         while runner.next is not None:

#             if runner.next.data == current.data:
#                 runner.next = runner.next.next

#             else:
#                 runner = runner.next

#         current = current.next


# remove_dupl(new_list)

# new_list.print_list()






_ = 'Interview Preparation Kit - Find Merge Point of Two Lists'



a = SinglyLinkedList()
[a.append(x) for x in [1,2,3]]

a_l = a._list_items()

b = SinglyLinkedList()
[b.append(x) for x in [1,2,3]]
b_l = b._list_items()


for i in range(len(a_l)):

    print(a_l[i] is b_l[i])


print (a_l == b_l)
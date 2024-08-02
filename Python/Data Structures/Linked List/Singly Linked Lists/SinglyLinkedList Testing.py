from gr_linked_lists import SinglyLinkedList, Node


'List creation test'
# new_linked_list = SinglyLinkedList()

# new_linked_list.head = Node('Albert')

# [new_linked_list.append(x) for x in ['Beth', 'George', 'Beth', 'Kathy', 'Beth', 'Ben']]
# new_linked_list.prepend('Jimmy')
# new_linked_list.insert_after('Jerome', 'Ben')
# new_linked_list.prepend('Kevin')
# new_linked_list.append('John')
# new_linked_list.delete('Kevin')
# new_linked_list.insert_after('Claude', 'Kathy')
# new_linked_list.delete('John')

# # new_linked_list.print_list()
# # print()

# new_linked_list.bubble_sort()

# # new_linked_list.print_list()
# # print()

# new_linked_list.reverse_list()

# new_linked_list.print_list()
# print()




'Sorting Test'
# new_list = SinglyLinkedList()

# [new_list.append(x) for x in 'CDBEA']

# new_list.print_list()
# new_list.bubble_sort()
# new_list.print_list()





'Interview Preparation Kit - Removing duplicates from a Linked List'


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






'Interview Preparation Kit - Find Merge Point of Two Lists'


# a = SinglyLinkedList()
# [a.append(x) for x in [1,2,3]]
# a_l = a._list_items()


# b = SinglyLinkedList()
# [b.append(x) for x in [0,2,3]]
# b_l = b._list_items()


# print()
# for i in range(len(a_l)):

#     print(f"is a[{i}]:'{a_l[i]}', b[{i}]:'{ b_l[i]}', Answer: {a_l[i] is b_l[i]}")


# print('\nIdentity Test for the two lists')
# print (f"list a:'{a_l}' is list b:'{b_l}', Answer: {a_l == b_l}")
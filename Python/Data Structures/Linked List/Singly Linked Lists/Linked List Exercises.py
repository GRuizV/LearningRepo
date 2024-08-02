from SinglyLinkedList import *
# from SinglyLinkedListBubbleSort import *


''' 
Here is how to merge two singly linked list
'''


first_list = SinglyLinkedList()

first_list.append(6)
first_list.append(3)
first_list.append(5)
first_list.append(1)
first_list.append(8)
first_list.append(4)
first_list.append(9)




second_list = SinglyLinkedList()

second_list.append(5)
second_list.append(8)
second_list.append(9)
second_list.append(5)
second_list.append(1)
second_list.append(7)


third_list = SinglyLinkedList()

third_list.append(4)
third_list.append(2)
third_list.append(1)
third_list.append(3)







'''Merging the lists'''

# print(f'the lists to be merged are: {first_list._list_items()} and {second_list._list_items()}')

# merged_list = first_list

# merged_list.extend_list(second_list)

# print(f'the merged list is: {merged_list._list_items()}')




''' Sorting the list '''

third_list.print_list()

third_list.bubble_sort_list()

third_list.print_list()



''' Reversing the list '''

# second_list.print_list()

# second_list.reverse_list()

# second_list.print_list()



''' Popping nodes from the list '''

# first_list.print_list()

# a = first_list.pop_node()
# print(a.data)

# first_list.print_list()

# a = first_list.pop_node(0)
# print(a.data)

# first_list.print_list()

# a = first_list.pop_node(2)
# print(a.data)

# first_list.print_list()

# a = first_list.pop_node(-2)
# print(a.data)

# first_list.print_list()


# a = first_list.pop_node(7)




''' 
4. Write a Python program to access a specific item in a singly linked list using index value.

'''

# second_list.print_list()

# print(second_list.data_in_index(5))




''' 
5. Write a Python program to set a new value of an item in a singly linked list using index value.
'''

# second_list.print_list()

# def change_data(self, index, new_data):

#     if self.is_empty():
#         return
    
#     ind = self._access_index(index)

#     current = self.head

#     for i in range(ind):

#         current = current.next

#     current.data = new_data


# change_data(second_list, -1, 'X')

# second_list.print_list()










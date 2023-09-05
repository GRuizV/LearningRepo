import math
from collections import deque, Counter


'Linked Lists - Find Merge Point of Two Lists'


# # the solution was as follows:

# def findMergeNode(head1, head2):
       
#     n1 = list()
#     n2 = list()
    
#     while head1:
#         n1.append(head1)            
#         head1 = head1.next
                
#     while head2:
#         n2.append(head2)            
#         head2 = head2.next
            
#     for i in n1:
#         for j in n2:
#             if i == j:
#                 return i.data

# # the only thing I didn't undertand was why just by comparing nodes and not the data in it, it finds the merging point




'Stacks and Queues - Balanced Brackets'


# s = '{{[[(())]]}}'
# # s = '({}([][]))[]()'


# stack = list()

# bracket_map = {')':'(', '}':'{', ']':'['}

# for bracket in s:

#     if bracket in '({[':
#         stack.append(bracket)

#     elif bracket in ')]}':

#         if len(stack) == 0:
#             print('NO')
#             break

#         stack_top = stack.pop()

#         if bracket_map[bracket] != stack_top:
#             print('NO')
#             break
    
#         print('YES')

# print()

# if len(stack) != 0:
#     print('Not Pass')

# else:
#     print('Pass')




'Queues: A Tale of Two Stacks'


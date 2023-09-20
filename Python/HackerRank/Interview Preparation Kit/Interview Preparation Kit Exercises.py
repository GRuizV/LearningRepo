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




'Stacks and Queues - Largest Rectangle'

''' 
First, I'm gonna try by brute force since it isn't evidently solvable with something I already know,
later I will try to find an optimal solution

'''

# buildings = [1, 2, 3, 4, 5, 1, 2, 4, 6]
# buildings = [1, 2, 3, 4, 5]
# buildings = [11,11,10,10,10]
buildings = [2,1,3,4,2,1,3,2,4]

rectangles = list()


# 1st approach
# for i in range(len(buildings)):

#     adj_buildings = list()

#     for j in range(i, len(buildings) ):

#         if buildings[j] < buildings[i]:
#             break

#         adj_buildings.append(buildings[j])

#     if j == len(buildings) - 1:
#         j = len(buildings)

#     rectangles.append( min(adj_buildings) *  len(buildings[i:j])  ) 



''' 
This second approach actually worked, but it has nothing to do with stacks nor Queues, and has a complexity of O(n)^2
I will research to understand the intention of the exercise and a optimal solution
'''

# # 2nd approach
# for i in range(len(buildings)):

#     adj_buildings = list()

#     for j in range(len(buildings[:i]),-1,-1):

#         if buildings[j] < buildings[i]:
#             break

#         adj_buildings.append(buildings[j])


#     for j in range(i+1, len(buildings)):

#         if buildings[j] < buildings[i]:
#             break

#         adj_buildings.append(buildings[j])


#     num_buildings = len(adj_buildings)
#     rectangle = num_buildings * buildings[i]
#     rectangles.append(rectangle)
    

# print(rectangles)

# print( max (rectangles) )




''' 
Finally the solution with stacks is below
    But, the logic behind it actually eludes me :/
'''

h = [2,1,3,4,2,1,3,2,4]

max_area = 0
stack = list()

for i, current_height in enumerate(h):

    start_position = i

    while stack and (stack[-1][1] > current_height):

        index, height = stack.pop()

        current_area = (i - index) * height

        max_area = max(max_area, current_area)

        start_position = index

    stack.append((start_position, current_height))

for i, current_height in stack:

    current_area = current_height * (len(h) - i)

    max_area = max(max_area, current_area)

print (max_area)
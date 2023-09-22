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

# # buildings = [1, 2, 3, 4, 5, 1, 2, 4, 6]
# # buildings = [1, 2, 3, 4, 5]
# # buildings = [11,11,10,10,10]
# buildings = [2,1,3,4,2,1,3,2,4]

# rectangles = list()


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

# h = [2,1,3,4,2,1,3,2,4]

# max_area = 0
# stack = list()

# for i, current_height in enumerate(h):

#     start_position = i

#     while stack and (stack[-1][1] > current_height):

#         index, height = stack.pop()

#         current_area = (i - index) * height

#         max_area = max(max_area, current_area)

#         start_position = index

#     stack.append((start_position, current_height))

# for i, current_height in stack:

#     current_area = current_height * (len(h) - i)

#     max_area = max(max_area, current_area)

# print (max_area)




'Stacks and Queues - Max Min Riddle'

'''
    Here I thik I got idea on how I can tackle the problem using a deque,
    but just as exercise to regain confidence I will try first by brute force
    and then try with a deque, which is my best guess at the moment

'''

'''
    Cases

    arr = [int(x) for x in '2 6 1 12'.split()] / sol: 12 2 1 1
    arr = [int(x) for x in '1 2 3 5 1 13 3'.split()] / sol: 13 3 2 1 1 1 1
    arr = [int(x) for x in '3 5 4 7 6 2'.split()] / sol: 7 6 4 4 3 2
    
'''


# arr = [2, 6, 1, 12]
# arr = [int(x) for x in '3 5 4 7 6 2'.split()]



# res = list()

# for i in range(1, len(arr)+1):

#     temp = list()

#     for j in range((len(arr)+1)-i):

#         temp.append(arr[j:j+i])

#     temp = map(min,temp)    
#     res.append(max(temp))

# print(res)


'''
Brute forcing it worked 70% but it isn't optimal since complexity goes up to O(N)^2

'''

'This is the farthest I got with my own knowledge'

# arr = [int(x) for x in '2 6 1 12'.split()]

# xdeque = list()

# for i in range(len(arr)):

#     mins = list()    
#     xdeque = arr[:i+1]
   
#     for j in range(len(arr)-1,0,-1):

#         mins.append(xdeque[:])
#         xdeque.pop(0)
#         xdeque.append(arr[-j+i])

#     print(mins)
#     print(xdeque)



'Here is the chatGPTs Solution for this - but how neccessary and practical is for me to have this kinds of solutions?'
'   Id like to discuss this with Juan'

def min_max_riddle(arr):
    n = len(arr)
    stack = []
    max_min = [0] * n

    # Iterate through the sorted array in descending order
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        j = stack[-1] if stack else -1
        max_min[i] = i - j - 1
        stack.append(i)

    # Process the max_min values to get the final answer
    result = [0] * (n + 1)
    for i in range(n):
        result[max_min[i]] = max(result[max_min[i]], arr[i])

    # Fill in any gaps in the result
    for i in range(n - 1, 0, -1):
        result[i] = max(result[i], result[i + 1])

    return result[1:]

# Example usage:
n = int(input())
arr = list(map(int, input().split()))
result = min_max_riddle(arr)
print(" ".join(map(str, result)))












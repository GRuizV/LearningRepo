import math
from collections import deque, Counter


_ = '2D Arrays - DS'

'Sketching the solution'

# a = '1 1 1 0 0 0 0 1 0 2 3 0 1 1 1 5 4 4'

# a = list(map(int, a.split()))

'''
[1, 1, 1, 0, 0, 0]
[0, 1, 0, 2, 3, 0]
[1, 1, 1, 5, 4, 4]
'''
# a = [x for x in (a[0:6], a[6:12], a[12:])]

# b =  list()

# # Grouping up hourglass items
# for i in range(4):

#     b.append([ a[0][i:i+3], a[1][i+1], a[2][i:i+3] ])

'''
[[1, 1, 1], 1, [1, 1, 1]]
[[1, 1, 0], 0, [1, 1, 5]]
[[1, 0, 0], 2, [1, 5, 4]]
[[0, 0, 0], 3, [5, 4, 4]]
'''
# for i in b: print(i)


# d = list()

# # Summing up elements
# for i in b:

#     d.append( sum(i[0]) + i[1] + sum(i[2])) 


# print(d)


'-----------------------------------------'

'Actual Problem'

# a = '1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0'

# a = list(map(int, a.split()))

# a = [x for x in ( a[0:6], a[6:12], a[12:18], a[18:24], a[24:30], a[30:] ) ]

# '''
# [1, 1, 1, 0, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [1, 1, 1, 0, 0, 0]
# [0, 0, 2, 4, 4, 0]
# [0, 0, 0, 2, 0, 0]
# [0, 0, 1, 2, 4, 0]
# '''
# # for i in a : print(i)

# b = list()

# for i in range(4):

#     for j in range(4):

#         b.append( [ a[i][j:j+3], a[i+1][j+1], a[i+2][j:j+3] ] )    



# '''
# [[1, 1, 1], 1, [1, 1, 1]]
# [[1, 1, 0], 0, [1, 1, 0]]
# [[1, 0, 0], 0, [1, 0, 0]]
# [[0, 0, 0], 0, [0, 0, 0]]
# [[0, 1, 0], 1, [0, 0, 2]]
# [[1, 0, 0], 1, [0, 2, 4]]
# [[0, 0, 0], 0, [2, 4, 4]]
# [[0, 0, 0], 0, [4, 4, 0]]
# [[1, 1, 1], 0, [0, 0, 0]]
# [[1, 1, 0], 2, [0, 0, 2]]
# [[1, 0, 0], 4, [0, 2, 0]]
# [[0, 0, 0], 4, [2, 0, 0]]
# [[0, 0, 2], 0, [0, 0, 1]]
# [[0, 2, 4], 0, [0, 1, 2]]
# [[2, 4, 4], 2, [1, 2, 4]]
# [[4, 4, 0], 0, [2, 4, 0]]
# '''
# # for i in b: print(i)

# c = list()

# for i in range(len(b)):
#     c.append( sum(b[i][0]) + b[i][1] + sum(b[i][2])  )



# res = max(c)

# print(res)




_ = 'Shelock and Squeares'

# a, b = 17, 24

# rang = range(a,b+1)

# # res = [ x for x in rang if math.sqrt(x) == int(math.sqrt(x)) ]

# # print(res)

# a,b = int(math.sqrt(24)) , int(math.sqrt(49))

# res = [x for x in range(a,b+1) if x**2 in rang]

# print(res)




_ = 'New Year Chaos'
 
# q = [2,1,5,3,4]

# bribes = 0

# for i in range(len(q)-1,0,-1):

#     if q[i] != i+1:

#         if q[i-1] == i+1:

#             bribes += 1

#             q[i-1], q[i] = q[i], q[i-1]

#         elif q[i-2] == i+1:

#             bribes += 2

#             q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]

#         else:

#             print('Too chaotic')
#             break


# print(bribes)




_ = 'Minimum Swaps'


# q = [x for x in map(int,'4 3 1 2'.split())]
# swaps = 0

# # [False, False, False, False, False]
# visited = [False]*len(q)

# for i in range(len(q)):

#     if visited[i] is False:

#         a = i
#         b = q[i] - 1
#         l = 1

#         visited[i] = True

#         while b != i:

#             visited[b] = True

#             a = b
#             b = q[b]-1
#             l += 1

#         swaps += l-1

# print(swaps)



_ = 'Array Manipulation'


# n = 10

# queries = [[1,5,3], [4,8,7], [6,9,1]]

# arr = [[0]*n]

# # print(arr)
# # print()

# for i in range(len(queries)):

#     j = i+1

#     row = arr[i]

#     hi = queries[i][1]+1
#     low = queries[i][0]
#     summand = queries[i][2]

#     row = row[:low-1] + [x + summand for x in row[low-1:hi-1]] + row[hi-1:]

#     arr.append(row)


# for i in arr:
#     print(i)
# print()


# ans = list(map(max,arr))

# print(max(ans))
# print()


#Essentially with this solution the problem is solved, but not scalable, so for hackerrank there has to be a more efficient way to do it in large scale.


x = '--------------------------------------------------'


# #ChatGPTs & some guy in the discussion section brought a solution base on the concepto of 'prefix sums'

# print()
# print('XXXXX Prefix Sums Solution XXXXX')
# print()


# def array_manipulation_2(n, queries):
            
#         ans = [0] * n
        
#         for i in queries:
            
#             a, b, k = i

#             ans[a-1] += k
            
#             if b < len(ans):
                
#                 ans[b] -= k
            
#             print(ans)
                           
                
#         current_sum = 0
#         max_value = 0
        
#         for i in range(len(ans)):
            
#             current_sum += ans[i]
            
#             max_value = max(max_value,current_sum)
            
#         return max_value


# sol = array_manipulation_2(n, queries)


# print()
# print(sol)






_ = 'Sorting - Mark and Toys'


# budget = 50

# toys = [1, 12, 5, 111, 200, 1000, 10]
# print(toys)




# # With Bubble Sort was not efficient enough
# swapped = True

# while swapped is True:

#     swapped = False
#     i = 0

#     while True:

#         if i == len(toys)-1:
#             break

#         if toys[i] > toys[i+1]:

#             swapped = True

#             toys[i], toys[i+1] = toys[i+1], toys[i]

#         i += 1



# # Let's try with Merge Sort

# def merge_sort(arr):

#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr)//2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     return merge(left, right)



# def merge(left, right): 

#     result = list()
#     i = j = 0

#     while i < len(left) and j < len(right):

#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1

#         else:            
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1
        
#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# toys = merge_sort(toys)

# print(toys)


# toys_purchased = list()
# spent = 0

   
# for i in toys:

#     toys_purchased.append(i)

#     spent += i

#     if spent > budget:

#         spent-= i
#         toys_purchased.pop()

#         break
       
        

# print(toys_purchased)




_ = 'Strings: Making Anagrams'


# import collections

# a = 'cde'
# b = 'abc'

# # a = 'cde'
# # b = 'dcf'


# a_s = set(a)
# b_s = set(b)

# common = a_s.intersection(b_s)
# diff = [x for x in a_s.difference(b_s)] + [x for x in b_s.difference(a_s)]

# deletions = 0

# for i in common:
#     deletions += abs(a.count(i)-b.count(i))

# for i in diff:
#     deletions += a.count(i) + b.count(i)


# print(deletions)




_ = 'Find Merge Point of Two Lists'


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




_ = 'Sorting: Comparator'

# # At base, the task is to sort descending first by score and ascending by name second

# a = [['amy', 100], ['david', 100], ['heraldo', 75], ['aakansha', 75], ['aleksa', 150]]

# a = sorted(a, key= lambda x: (-x[1], x[0])) # Fundamentally, here's the answer.
# # a = sorted(a, key= lambda x: -x[1])
# # a = sorted(a, key= lambda x: (x[1], x[0]))

# print(a)




_ = 'String Manipulation - Alternating Characters'

# s = ['AAAA', 'BBBBB', 'ABABABAB', 'BABABA', 'AAABBB']

# for str in s:

#     deleted = 0

#     i = 0
#     j = 1

#     while True:

#         if j == len(str): 
#             break       

#         if str[i] == str[j]:
#             deleted += 1
#             j += 1

#         else:
#             i = j
#             j += 1

#     print(deleted)




_ = 'String Manipulation - Sherlock and the Valid String'

# from collections import Counter

# s = 'abcdefghhgfedecba'

# s = Counter(s)

# val = sorted(s.values())

# def test(s):
#     res = all( [x == s[0] for x in s] ) 
#     return res

# if test(val):
#     print('YES')

# elif test(val[1:]):  
#     print('YES')

# else:

#     val[-1]-=1
#     if test(val):        
#         print('YES')

#     else:       
#         print('NO')




_ = 'Special String Again'


# # My solution worked but wasn't scalable enough

# s = 'mnonopoo'


# def is_special(s): 
    
#     test1 = False
#     test2 = False

#     if all(x == s[0] for x in s):
#         test1 = True

#     if len(s) > 1 and len(s)%2 != 0 and all(x == s[0] for x in s[0:len(s)//2]+s[len(s)//2+1:]):
#         test2 = True

#     if test1 or test2:
#         return True
    
#     else:
#         return False


# def subs_gen(s):

#     subs = list()
   
#     for i in range(1, len(s)+1):
        
#         for j in range( (len(s)+1) - i ):

#             subs.append(s[j:j+i])
    
#     res = [x for x in subs if is_special(x)]

#     return res


# print(subs_gen(s))


x = '--------------------------------------------'


# #Some other guy's solution

# def substrCount(n, s):

#     nsubs, nchars, ch = 1, 1, s[0]

#     for i in range(1,n):

#         if ch == s[i]:

#             nchars += 1
#             nsubs += nchars

#         else:

#             for j in range(i+1, min(n, i+1+nchars)):

#                 if s[j] != ch:                    
#                     break

#                 nsubs += 1

#             ch, nchars = s[i], 1

#             nsubs += 1

#     return nsubs




'Sorting - Fraudulent Activity Notifications'


# # exp = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# # exp = [1,2,3,4,4]
# exp = [10, 20, 30, 40, 50]

# # d = 5
# # d = 4
# d = 3



' My solution'

# notifications = int()

# exp_base = sorted(exp[:d])

# if d % 2 == 0:
#     median = sum([exp_base[d//2-1], exp_base[d//2]]) / 2

# else:
#     median = exp_base[d//2]


# for i in exp[d:]:
    
#     if i >= 2 * median:
#         notifications += 1


# print(notifications)




"   ChatGPT's solution - Sliding window for meadian algorithm "


# def activity_notifications(expenditure, d):

#     def get_median(count_array, d):

#         if d % 2 == 1:

#             # For odd days, the median is the middle value
#             middle_index = d // 2

#             for i, count in enumerate(count_array):

#                 middle_index -= count

#                 if middle_index < 0:
#                     return i
                
#         else:

#             # For even days, the median is the average of two middle values
#             first_middle = None
#             second_middle = None
#             middle_count = 0

#             for i, count in enumerate(count_array):

#                 middle_count += count

#                 if middle_count >= d // 2 and first_middle is None:
#                     first_middle = i

#                 if middle_count >= d // 2 + 1 and second_middle is None:
#                     second_middle = i                    
#                     break

#             return (first_middle + second_middle) / 2


#     n = len(expenditure)

#     fraud_count = 0

#     # Initialize the count array for the first d days
#     count_array = [0] * 201

#     for i in range(d):
#         count_array[expenditure[i]] += 1


#     for i in range(d, n):
#         median = get_median(count_array, d)
#         if expenditure[i] >= 2 * median:
#             fraud_count += 1
#         print(f'\nmedian: {median}\n')
#         # Update the count array for the sliding window
#         count_array[expenditure[i - d]] -= 1
#         count_array[expenditure[i]] += 1

#     return fraud_count


# res = activity_notifications(exp,d)

# print(res)






_ = 'String Manipulation - Common Child'



# s1 = 'SHINCHAN'
# s2 = 'NOHARAAA'


x = '--------------------------------------------'

# # My solution worked on 2 of the 3 run cases. 

# ind_1 = int()
# res = list()
# ind_2 = int()
# child = str()
# i = int()


# while i <= len(s1):

#     if i == len(s1):
#         break

#     j = 0    

#     if ind_2 != 0 or s2[ind_2] in child:  # And s1[ind2] not in child
#         j = ind_2 + 1

#     while j < len(s2):
        
#         if s1[i] == s2[j]:
            
#             if ind_2 == 0 and s2[ind_2] not in child: # And s1[ind2] not in child
#                 ind_1 = i  

#             child += s1[i]
#             ind_2 = j
#             break
        
#         j += 1
    
#     i += 1

#     if i == len(s1):

#         res.append([child, ind_1])
#         child = str()
#         i = ind_1 + 1
#         ind_2 = 0

# res = sorted(res, key = lambda x: len(x[0]))

# sol = len(res[-1][0])

# print(res)
# print(sol)



x = '--------------------------------------------'


#Some other guy's solution

# This problem was resolved by this guy using an application of the LCS (Longest Common Substring) Algorithm


# s1 = 'SHINCHAN'
# s2 = 'NOHARAAA'


# prev = [-1 for i in range(len(s2)+1)]

# for i in range(len(s1),-1,-1):

#     curr = [-1 for i in range(len(s2)+1)]

#     for j in range(len(s2),-1,-1):

#         if i==len(s1) or j==len(s2):

#             curr[j] = 0

#         else:

#             if s1[i]==s2[j]:
#                 curr[j] = 1 + prev[j+1]

#             else:
#                 curr[j] = max(prev[j], curr[j+1])

#     prev = curr

# print(prev)




_ = 'Hash Table: Ransom Notes'


# m = 'ive got a lovely bunch of coconuts'
# n = 'ive got some coconuts'

# dict_n1 = {k:n.count(k) for k in n.split()} # What I need
# dict_n2 = {k:m.count(k) for k in n.split()} # What I count with



# #This was my first solution
# # print(list(zip(dict_n1.values(), dict_n2.values())))

# x = all([x[0]<=x[1] for x in zip(dict_n1.values(), dict_n2.values())])

# # print(dict_n1)
# # print(dict_n2)

# print('Yes') if x else print('No')




# # This was my second solution
# res = sorted(list(map(lambda x: x[1]-x[0],zip(dict_n1.values(),dict_n2.values()))))

# print('Yes') if res[0] >= 0 else print('No')




# # This solution came from ChatGPT

# dict_n1 = {k:n.count(k) for k in n.split()} # What I need
# dict_n2 = {k:m.count(k) for k in m.split()} # What I count with

# res = True

# for word, count in dict_n1.items():
#     if word not in dict_n2 or dict_n2[word] < count:
#         res = False

# print('Yes') if res else print('No')

# # At the very end of the exercise, this strategy of accessing the word in the second dictionary was key but also importing Counter from collections since..
# # the first two comprehensions still were consuming resources.




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


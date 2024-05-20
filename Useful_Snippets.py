from timeit import default_timer as timer
import random
import itertools


''' Prime numbers' sieve '''

# def primeNumbers (cap):

#     primes, non_primes  = [1], list()

#     for i in range(2, cap + 1):

#         if i not in non_primes:     
            
#             primes.append(i)

#             for j in range( i*i , cap + 1, i):    non_primes.append(j)

#     return primes 

# prime_test = primeNumbers(30)

# print(prime_test)





''' Using eval() To evaluate something for each element of a list '''


# li = [1, 3, 5, 7, 11]
	
# cap = max(li)


# def isPrime (n, cap):   

#     primes, non_primes  = [1], list()

#     for i in range(2, cap + 1):

#         if i not in non_primes:     
            
#             primes.append(i)

#             for j in range( i*i , cap + 1, i):    non_primes.append(j)

#     if n in primes: return True

#     else: return False

# print( ( [ eval( f'isPrime({i},{cap})') for i in li ] ) )   #This shows the eval on each element of the list

# print( all( [ eval( f'isPrime({i},{cap})') for i in li ] ) ) #This line here, tells if every element in the list is a prime number





''' Ordering a dict by values '''


# dict1 = {'A': 100, 'B': 550, 'C': 948, 'D': 95, 'E': 12}

# sorted_dict = { k: v for k, v in sorted( dict1.items(), key = lambda x: x[1], reverse = False ) } # Ascending Order

# print(sorted_dict)





''' Flattening an Array with ListComp '''

# vec = [[1,2,3], [4,5,6], [7,8,9]]
	
# new_list = [num for elem in vec for num in elem]
	
# print(new_list)





''' Transposing a matrix with ListComp & zip( ) functions '''

 
# matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]


# # ListComp
# transp_matrix = [ [ elem[i] for elem in matrix] for i in range(len(matrix[0])) ]

# print(transp_matrix)


# # Using Zip()
# transp_matrix = list( map( list, zip(*matrix) ) )

# print(transp_matrix)



''' ---------- '''


# Most basic loop way to do it
# transp_matrix = [  ]

# for i in range(len(matrix[0])):

#     temp = list()

#     for j in range(len(matrix)):

#         temp.append(matrix[j][i])

#     transp_matrix.append(temp)

# print(transp_matrix)





''' Creating multiple lists quickly '''

# n = 3

# lists = { f'list {i}' : list() for i in range(1, n + 1)   }

# print(lists)





''' Base sorting algorythm '''

# import random


# # Initialize array     
# arr = [random.randint(0,11) for x in range(10)] 

# # Displaying elements of original array    
# # print(f'Elements of the original array: {arr}')    

# s = timer()  

# #Sort the array in ascending order    
# for i in range( len(arr) ): 

#     for j in range( i + 1, len(arr) ): 

#         if(arr[i] > arr[j]):  # '>' will set an asceding order and '<' will set descending 

#             arr[i], arr[j] = arr[j], arr[i]

# e = timer()     

# # Displaying elements of the array after sorting        
# # print(f'Elements of array sorted in ascending order: {arr}', e-s )

# print(e-s)


''' My version of the algorythm without double iteration '''

# import random

# arr = [9, 1, 10, 8, 9, 9, 8, 7, 1, 9] 


# print(f'Array before sortring {arr}')

# for i in range( len(arr) - 1 ):

#     li = arr[ i - len(arr) : ]

#     index = li.index( min( li )) + i

#     if arr[i] > arr[ index ]:  
        
#         arr[i], arr[ index ] = arr[ index ], arr[i]

      
# print(f'Array after sortring {arr}')





''' Taking unique values from a list of dicts '''

# base = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

# base = { v for item in base for v in item.values() }

# print(base)






''' Combining elements of a list of lists without considering order '''

# # First, just as test let's try to combine with regular number of items

# # Initilizing the base list:
    
#     # [3]x[Ir] / [['a', 'b'], ['g'], ['i', 'j']]
#     # [3]x[2] /  [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] /  [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]



# base = [['a', 'b'], ['g'], ['i', 'j']]


# # This will be the combinations container
# comb = list()


# # The looping solution would be:

# s = timer()


# for i in range( len(base) -1 ):

#     for j in range( len(base[i]) ): 

#         for k in range( i+1, len(base) ):
            
#             for l in range( len(base[k]) ):

#                 comb.append(f'{base[i][j]}{base[k][l]}')

# e = timer()

# print(comb, (e-s))

'This solution showed to be working just fine'



'----------'

# # This is a Listcomp solution for the same problem


# # Initilizing the base list:
    
#     # [3]x[Ir] / [['a', 'b'], ['g'], ['i', 'j']]
#     # [3]x[2] /  [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] /  [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]



# base = [['a', 'b'], ['g'], ['i', 'j']]

# comb = list()

# s = timer()

# for i in range( len(base) - 1 ):

#     for j in range( len( base[i] )):

#         temp_list = [ f'{base[i][j]}{x}' for x in [ x for elem in base[ i + 1: ] for x in elem ] ] 

#         comb.extend(temp_list)

# e = timer()

# print(comb, (e-s))

'This solution also works but showed to be less efficient than the nested for loops one'







''' Combining the elements of a list of lists considering order  '''


# # Initilizing the base list:

#     # [3]x[2] / [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] / [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]



# base = [['a', 'b'], ['c', 'd'], ['e', 'f']]


# # This will be the combinations container
# comb = list()

# s = timer()

# for i in range(len(base)):

#     for j in range(len(base[i])):

#         for k in range(len(base)):

#             if k == i:

#                 continue

#             else:

#                 for l in range(len(base[k])):
                    
#                     comb.append( f'{base[i][j]}{base[k][l]}' )

# e = timer()

# print( comb, (e-s) )

'This solution showed to be working just fine'




'----------'

# # This is a Listcomp solution for the same problem


# # Initilizing the base list:

#     # [3]x[2] / [['a', 'b'], ['c', 'd'], ['e', 'f']]
#     # [3]x[3] / [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]


# base = [['a', 'b'], ['c', 'd'], ['e', 'f']]

# comb = list()

# s = timer()

# for i in base:

#     for j in i:

#         temp_list = [f'{j}{x}' for x in [x for elem in base[:base.index(i)] + base[base.index(i)+1:] for x in elem] ]

#         comb.extend(temp_list)

# e = timer()
       
# print(comb, (e-s))


'This solution also works but showed to be less efficient than the nested for loops one'





'''
The first recursion problem I review:

    54. Write a Python program to get the depth of a dictionary.

        Expected Output: 4
    
'''

# d = {'a':1, 'b': {'c': {'d': {}}}}

# def dict_depth(d):

#     if isinstance(d, dict):

#         return 1 + (  max( map ( dict_depth, d.values() ) ) if d else 0 )       # is not that clear to my why it work only with the max() function.
    
#     return 0

# print(dict_depth(d))





'''A Fibonacci Generator'''

# def fibonacci_nums(x=0, y=1):

#     yield x

#     while True:

#         yield y

#         x, y = y, x + y





'''Merging dictionaries'''


'To sum up the |= operator does the sames as the dict.update() function'

# user_base_data = {

#     'name' : 'xxxxx',
#     'last_name' : 'xxxxx',
#     'phone' : 'xxxxxx',
#     'address' : 'xxxx'

# }


# george_data = {

#     'name' : 'George',
#     'last_name' : 'Smith',
#     'phone' : '555-55-55',
   
# }


# user_base_data |= george_data

# print(user_base_data)



# user_base_data.update(george_data)

# print(user_base_data)'''A Fibonacci Generator'''

# def fibonacci_nums(x=0, y=1):

#     yield x

#     while True:

#         yield y

#         x, y = y, x + y





'''Sorting with 2 criteria'''

# # The goal is to pick the three most reppeated letters and also in alphabetical order

# # First will be sorted by occurrence and the alphabetically

# s = 'aaeebbbccd'

# d = { c : s.count(c) for c in s }

# print(d)    # {'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 1}


# d = sorted(d.items(), key = lambda x: x[1], reverse = True)

# print(d)    # [('b', 3), ('a', 2), ('e', 2), ('c', 2), ('d', 1)]

# print(d[:3])    # [('b', 3), ('a', 2), ('e', 2)]
# # Here there is the problem: 'a', 'e' and 'c' have the same ocurrences and if we pick the top three just like that,
# # 'c' would be cut out, giving that 'e' should not make the cut instead of 'c'


# 'Here is the solution: the key kwarg give the chance to pass a tuple to consider two criterias at the same time'
# d = sorted(d.items(), key = lambda x: (x[1], x[0]) , reverse = True)

# print(d)    # [('b', 3), ('e', 2), ('c', 2), ('a', 2), ('d', 1)]
# # But the thing is that as reverse kwarg is set in True, it also affects the second criteria x[0], so it returns alphabetically second to ocurrence
# # but, in ascending order, and we need it in descending order 


# # if we try just to set reverse to False, the problem is that also affects the criteria x[1]
# d = sorted(d.items(), key = lambda x: (x[1], x[0]) , reverse = False)

# print(d)    # [('d', 1), ('a', 2), ('c', 2), ('e', 2), ('b', 3)]

# # So to overcome this issue, the solution is to change the occurrence criteria from x[1] to -x[1], that will make it be descending without the reverse kwarg


# d = sorted(d.items(), key = lambda x: (-x[1], x[0]))

# print(d)    # [('b', 3), ('a', 2), ('c', 2), ('e', 2), ('d', 1)]


# 'Solving definitively the problem in case'

# print(d[:3])    # [('b', 3), ('a', 2), ('c', 2)]






''' Unknown number of inputs for a HackerRank problem '''

'''

    Task

    Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
    You will then be given an unknown number of names to query your phone book for. 
    For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
    if an entry for  is not found, print Not found instead.


    input

    ... After the  lines of phone book entries, there are an unknown number of lines of queries. 
    Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.


'''


# N = int(input().strip())

# d = dict()

# for i in range(N):

#     inp = input().strip().split()

#     d[inp[0]] = inp[1]



# while True:

#     try:

#         name = input().strip()

#         inp = d.get(name,'Not found')

#         if inp == 'Not found':
#             print(inp)
        
#         else:
#             print(f'{name}={d[name]}')

#     except EOFError:
#         break




# _ = 'How to create all possible substrings from a string'


# s = 'abcd'

# subs = list()

# #[1,2,3,4]
# for i in range(1, len(s)+1):

#     # R/ 4:[0,1,2,3] ; 3: 
#     for j in range( (len(s)+1) - i ):

#         subs.append(s[j:j+i])


# print(subs) # R/ ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']







'This is a Index Handler (made by me) to deal with indexes while working with DataStructures '

# def _index_handler(self, index):

#     if self.is_empty():
#         return

#     if index > (self.len()-1) or index < -self.len():
#         raise IndexError('Index out of range')
    
#     # converting the index into a positive index
#     if index < 0: 

#         norm_index = range(self.len())
#         inv_index = range(-len(norm_index),0)
#         dict_index = {k:v for k,v in zip(inv_index, norm_index)}

#         return dict_index[index]

#     else:

#         return index  








'Slinding window for median calculation'

# data = [random.randint(0,9) for _ in range(9)]

# sliding_size = 5

# print(f'Base data: {data}\n')


# def get_median(count_array, d):

#     if d % 2 == 1:

#         middle_index = d // 2

#         for i, count in enumerate(count_array):

#             middle_index -= count

#             if middle_index < 0:

#                 return i
    
#     else:

#         first_middle = None
#         second_middle = None
#         middle_count = 0

#         for i, count in enumerate(count_array):

#             middle_count += count

#             if middle_count >= d // 2 and first_middle is None:

#                 first_middle = i

#             if middle_count >= d // 2 + 1 and second_middle is None:

#                 second_middle = i

#                 return (first_middle + second_middle) / 2


# n = len(data)

# # the '10' is the max value the data could be, so it will count occurrences by each data item
# count_array = [0]*10

# # Counting occurrences
# for i in range(sliding_size):
#     count_array[data[i]] += 1


# for i in range(sliding_size, n):

#     median = get_median(count_array, sliding_size)
#     unsorted_slice = data[i-sliding_size:i]
#     sorted_slice = sorted(data[i-sliding_size:i])

#     print(f'base median piece: {unsorted_slice}\nsorted base median piece: {sorted_slice}\nmedian: {median}\n')

#     # Update the count_array

#     count_array[data[i - sliding_size]] -= 1
#     count_array[data[i]] += 1







'Test to check if two elements contains the same elements'

# def have_same_elements(list1, list2):
#     return all(element in list1 for element in list2)

# a = ['a', True, 15]

# b = [15, 'a', True, 0]

# print(have_same_elements(a,b))






'Comming from Python 3.12'


'Accesing local variables within a function'

#     # with Python 3.12, a local() function called inside a function will return the local variables in a dict

# def foo():

#     x = str()
#     y = int()
#     z = [1,2,3]
#     w = dict()

#     print(locals())

# foo()   # {'x': '', 'y': 0, 'z': [1, 2, 3], 'w': {}}







'Batched method in itertools'

# li = [1,2,3,4,5,6,7,8,9,10,11]

# batches = itertools.batched(li,3)

# # [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11)]
# print(list(batches))







"My definitive version of Fibonacci's seq. generator based on recursion"

# def fib_seq(n):

#     def fibonacci(n):

#         if n == 0: return 0
#         if n == 1: return 1
        
#         return fibonacci(n-2) + fibonacci(n-1)
    
#     result = [0,1]

#     [result.append(fibonacci(i)) for i in range(2, n+1)]
#     return result







"b001 - The Even Groups Problem"

'''
    Create a function, split_integer(), that takes two integers as inputs, a and b,
    the integer a needs to be split into b groups as evenly as possible:

        e.g.:

            split_integer(7, 3) -> [2,2,3]
            split_integer(3, 5) -> [0,0,1,1,1]
            split_integer(10, 4) -> [2,2,3,3]
            
'''


# # My version
# def split_integer(num, parts):

#     quotient, remainder = divmod(num, parts)

#     result = [quotient for part in range(parts)]

#     for i in range(remainder):
#         result[i%len(result)] += 1

#     return result[::-1]


# # b001 version
# def split_integer(num, parts):

#     # step #1: retrive the quotient and the remainder (The most important)
#     quotient, remainder = divmod(num, parts)

#     # step #2: pull the number of parts that will be the qoutient straight
#     base_part_count = parts - remainder

#     # step #3: Make a list with the base parts
#     base_parts = [quotient] * base_part_count

#     # step #4: Make a list with the additional parts with the extra from the remainder
#     extra_parts = [quotient + 1] * remainder

#     return base_parts + extra_parts


# test_1 = print('Test #1: Pass') if split_integer(7, 3) == [2,2,3] else print('Test #1: Failed')
# test_2 = print('Test #2: Pass') if split_integer(3, 5) == [0,0,1,1,1] else print('Test #2: Failed')
# test_3 = print('Test #3: Pass') if split_integer(10, 4) == [2,2,3,3] else print('Test #3: Failed')


'''
    Note:
        First the knowledge of the use of the divmod() was crucial here, but that aside,
        the way b001 wrote the function was way more readable and self explanatory than mine.
        I think that is the difference between a newbie and someone with experience.
'''







"My Version of the Minimum Common Multiple Algorithm"


# def mcm(a):

#     # Auxiliary primes function
#     def primes(num):

#         primes = [1]
#         not_primes = list()

#         for i in range(2, num+1):

#             if i not in not_primes:
#                 primes.append(i)

#             for j in range(i+i, num+1, i):
#                 not_primes.append(j)

#         return primes


#     a_mcm = list()

#     while a != 1:

#         a_primes = primes(a)[1::]

#         for i in a_primes:

#             if a % i == 0:
#                 a_mcm.append(i)
#                 a //= i
#                 break
  
'''
    Note:
        During the work on the greatest common divisor recursion challenge given by ChatGPT,
        I developed my own version of the 'Minimum Common Mutiple' algorithm.
'''







"A Recursive Nested List Sum: It is actually the recursive way to travere Nested Lists"

'''
    Test Data: [1, 2, [3, 4], [5, 6]]
    Expected Result: 21
'''

# def rec_sum(lst):

#     total = 0

#     for elem in lst:

#         if isinstance(elem, list):
#             total += rec_sum(elem)           
        
#         else:
#             total += elem

#     return total

# data = [1, 2, [3, 4], [5, 6]]
# print(rec_sum(data))    # Result: 21







"A Non-Recursive way to traverse a Nested List"

# def item_counter(item_list):

#     count = 0
#     stack = list()
#     element = item_list
#     i = 0

#     while True:

#         if i == len(element):

#             if element == item_list:
#                 return count
            
#             else:
#                 element, i = stack.pop()
#                 i += 1
#                 continue
            

#         if isinstance(element[i], list):

#             stack.append([element, i])
#             element = element[i]
#             i = 0
            
#         else:
#             count += 1
#             i += 1







"A recursive solution for the Tower of Hanoi"


# def hanoi(n, start, end):
    
#     if n == 1:
#         print(f"from {start} to {end}")

#     else:
#         other = 6 - (start + end)
#         hanoi (n-1, start, other)
#         print(f"from {start} to {end}")
#         hanoi(n-1, other, end)






"Ternary operator and the 'or' as an assignment"

# # This is how the ternary operator works
# name = input('User name: ') 

# name = name if name else 'N/A'

# print(name)


# # and this does exactly the same with the use of the 'or'
# name2 = input('User name: ') 

# name2 = name or 'N/A'

# print(name2)







"Josephus Permutation Problems and Efficiency with Deques"


'''
    The problem states a group of soldiers that are planing to execute each other in a way that only one has to commit suicide.
    The problem is how to know at which position the soldier will have to execute himself, if the executioner will do it every k soldiers,
    is also requested to return the sequence of soldiers, being the last item the position requested.

    Later, the efficiency comes as a problem since if is a solution based on lists, looping and poping items would result in a O(n^2) complexity,
    then, Deques come handy

'''


# # Josephus Permutation Solution based on lists

# from timeit import default_timer as timer

# def solution(arr, k):

#     perm = list()
#     index = 0

#     while arr:

#         index = (index + k - 1) % len(arr)
#         item = arr.pop(index)
#         perm.append(item)
    
#     return perm


# n_soldiers = 7
# soldiers = [s+1 for s in range(n_soldiers)]
# k = 3
# result = solution(soldiers, k)


# # expected solution: [3,6,2,7,5,1,4]
# print(result)   # [3, 6, 2, 7, 5, 1, 4]


        
# # Efficiency measurement to list's solution



# n_soldiers = 1_000_000
# soldiers = [s+1 for s in range(n_soldiers)]
# k = 3

# s = timer()
# result = solution(soldiers, k)
# e = timer()

# print(f'{e-s:.2f}s')    # result: 234.40s



# # Josephus Permutation Solution based on Deques
# from collections import deque

# def deque_solution(arr, k):

#     arr = deque(arr)
#     perm = deque()
  
#     while arr:

#         arr.rotate(1-k)
#         item = arr.popleft()
#         perm.append(item)
    
#     return perm


# n_soldiers = 7
# soldiers = [s+1 for s in range(n_soldiers)]
# k = 3
# result = deque_solution(soldiers, k)

# # expected solution: [3,6,2,7,5,1,4]
# print(result)   # deque([3, 6, 2, 7, 5, 1, 4])

        
# # Efficiency measurement to deque's solution
# n_soldiers = 1_000_000
# soldiers = [s+1 for s in range(n_soldiers)]
# k = 3

# s = timer()
# result = deque_solution(soldiers, k)
# e = timer()

# print(f'{e-s:.2f}s')    # result: 0.26s

'''
    *Conclusions*

    There's a substantial difference between the implementations with lists
    vs the one with deques and this is due to the way python work with each one underneath
    with the lists, in order to be efficient in indexing, it stores neighborly each element of the list
    and when it comes to the pop operation, all elements from the popped one on needs to be move one to the left,
    making it inefficient working with big numbers...

    while, with the deques solution, this data structure does not need to have contiguously all the data from the deque,
    instead, it stores it in the memory with a pointer to the next item (kinda like in a linked list), with this, everytime
    an element is popped, instead of moving the whole structure over, it just reassign the pointer to the next element, which
    has a complexity of O(1),

    That's why there is such a big difference between the two implementations.
'''







"xxx"
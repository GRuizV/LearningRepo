
import random
from timeit import default_timer as timer
import string


'''
    5. Write a Python program to count the number of strings where the string length is 2 or more 
    and the first and last character are same from a given list of strings.

    Sample List : ['abc', 'xyz', 'aba', '1221']

    Expected Result : 2
'''

# li = ['abc', 'xyz', 'aba', '1221']

# # Listcomp approach

# res = [ x for x in li if len(x) >= 2 and x[0] == x[-1] ]

# len_res = len(res)

# print(len_res)


# # for loop approach

# c = 0

# for i in li:

#     if len(i) >= 2 and i[0] == i[-1]:

#         c += 1

# print(c)



'''
   6. Write a Python program to get a list, sorted in increasing order 
   by the last element in each tuple from a given list of non-empty tuples. 

    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

# # Lambda functions approach

# li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# sort_li = sorted( li, key = lambda x: x[1], reverse = False )

# print(sort_li)



# # for loop approach

# # li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# li = [(3, 5), (1, 5), (7, 4), (2, 9), (3, 1)]

# print(li)

# rev_li = []

# res_li = []

# rev_res_li = []

# for i in li:
#   rev_li.append((i[-1],i[0]))


# while len(rev_li) > 0:
#   res_li.append( rev_li.pop( rev_li.index( min(rev_li) ) ) )
   

# for i in res_li:
#   rev_res_li.append((i[-1],i[0]))

# print(rev_res_li)




# # Page's solution with sorted without lambda

# def last(n): return n[-1]   #Solved with an intermediate function

# li = [(1, 2), (4, 4), (2, 3), (2, 1), (2, 5)]

# print(li)

# li = sorted(li, key = last, reverse = False)

# print(li)




'''
  7. Write a Python program to remove duplicates from a list. 

'''


# # Eliminating duplicates thru a set

# li = ['A', 'A', 'B', 'C', 'D', 'D', 'E', 'F', 'G']

# res_li = set(li)

# res_li = sorted(list(res_li))

# print(res_li)


# # thru for / while looping

# li = ['A', 'A', 'B', 'C', 'D', 'D', 'E', 'F', 'G']

# for i in li:

#   c = li.count(i)

#   while c > 1:

#     li.remove(i)

#     c-=1 

# print(li)




'''
  10. Write a Python program to find the list of words that are longer than n from a given list of words. 

'''

# s = 'The quick brown fox jumps over the lazy dog'

# char_len = 5


# # listcomp

# words = [ word for word in s.split() if len(word) >= char_len]

# print(words)


''' ------------ '''


# # for loop

# words = []

# for i in s.split():

#     if len(i) >= char_len:
#         words.append(i)

# print(words)




'''
  11. Write a Python function that takes two lists and returns True if they have at least one common member.

'''

# # Checking membership thru sets

# l1 = [random.randint(1, 26) for x in range(20)]

# print(l1)

# l2 = [random.randint(24, 100) for x in range(20)]

# print(l2)


# res = False

# for i in set(l1):

#     if i in set(l2): res = True

# print(res)





'''
  16. Write a Python program to generate and print a list of first and last 5 elements 
  where the values are square of numbers between 1 and 30 (both included).

'''

# li = [ x**2 for x in range(1,31)]

# li = li[:6] + li[-5:]

# print(li)



'''
  17. Write a Python program to generate and print a list except for the first 5 elements, 
  where the values are square of numbers between 1 and 30 (both included)

'''

# li = [ x**2 for x in range(1,31)]

# li = li[5:]

# print(li)





'''
  19. Write a Python program to get the difference between the two lists

'''

# first_list = [1, 2, 3, 3, 4, 4, 7, 8, 9, 10]

# print(first_list)

# second_list = [1, 1, 1, 2, 4, 4, 4, 5, 6, 9]

# print(second_list)


# common, diff = list(), list()


# for elem in first_list:

#   if elem in second_list:

#     common.append(elem)
#     second_list.remove(elem)
  
#   else: diff.append(elem)

# diff.extend(second_list)
# diff.sort()

# print(f'Difference between lists: {diff}')
# print(f'Common elements between lists: {common}')




'''
  28. Write a Python program to find the n(input) largest number in a list.

'''

# li = [random.randint(1,10) for x in range(10)]

# print(li)

# n = int(input(f'Number up to {len(set(li))} max: '))

# order = sorted( list( set(li) ), reverse = True)

# print(sorted(li, reverse = True))

# print(f'the #{n} largest number is {order[n-1]}')


''' ----------- '''

# li.sort()

# print(f'\n{li}')

# li2 = list(set(li))

# for i in range(n-1):
#     li2.remove(max(li2))

# print(f'\nthe {n} max is: {max(li2)}')




'''
  30. Write a Python program to get the frequency of the elements in a list. 

'''

# li = sorted([random.randint(1,5) for x in range(20)])

# print(li)

# set1 = set(li)

# result = dict()

# for elem in set1:

#   result[f'{elem}'] = li.count(elem)

# result = { k : v for k,v in sorted( result.items() , key = lambda x : x[1], reverse = True )  }

# print(result)


''' ----------- '''


# set1 = set(li)

# for i in set1:
#   print(f'element "{i}": {li.count(i)}')





'''
  34. find all the prime numbers up to n. 

'''

n = 30

''' ----------- '''

# # This was my original approach

# primes = [1]

# for i in range( 2, n+1):
    
#   temp = []

#   for j in range( 2, i):
     
#     temp.append( i % j )
  
#   if 0 not in temp: primes.append(i)


# print(primes)


      
''' ----------- '''


# # This is Erastothenes Sieve's approach made by me

    
# primes_list = [1]

# not_primes = []


# for i in range(2, n+1):
    
#   if i not in not_primes:

#     primes_list.append(i)

#     for j in range( i*i, n+1, i):

#       not_primes.append(j)

    
# print(primes_list)




'''
  38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.

n = 1
Sample list: [0, 1, 2, 3, 4, 5]
Expected Output: [1, 0, 3, 2, 5, 4] 

'''


# # My Approach:

# n = 3

# li = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

# print(li)

# c = 1

# for v, i in enumerate(li):

#   if len(li) % n == 0 and v == len(li) - 1: continue 
  
#   elif c == n:

#     li.insert(v, li[v+1])

#     del li[v+2]

#     c = 1

#   else: 

#     c += 1 

# print(li)

    


'''
  41. Write a Python program to create multiple lists.

'''

# n = int(input('How many list will it be? '))

# lists = {}

# for i in range(1, n+1):
    
#     lists[str(i)] = []

# print(lists)




'''
  42. Write a Python program to find missing and additional values in two lists.

'''

# # My Approach

# li1 = ['A', 'B', 'C', 'D', 'E', 'F']

# li2 = ['D', 'E', 'F', 'G', 'H', 'I']


# missing =  [ x for x in li1 if x not in li2]

# additional = [ x for x in li2 if x not in li1]

# print(f'Missing: {missing}\nAdditional: {additional}')


# # Page's Approach with set usage

# set1, set2 = set(li1), set(li2)

# print(f'Missing: {set1.difference(set2)}\nAdditional: {set2.difference(set1)}')




'''
  43. Write a Python program to split a list into different variables.

'''

# #Page's Approach with lib's unpacking

# colors = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"), ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]

# var1, var2, var3 = colors

# print(f'{var1}\n{var2}\n{var3}')




'''
  44. Write a Python program to generate groups of five consecutive numbers in a list.

'''

# # My listcomp approach

# n = 50

# li = [ [ num for num in range(x, x+5) ] for x in range(1, 50, 5) ]

# print(li)


''' ---------- '''

# # My approach with for loops

# temp = []

# for i in range(1, n+1):

#   temp.append(i)

#   if len(temp) == 5:
    
#     li.append(temp)
    
#     temp = []

  
# print(li)


''' ---------- '''

# #Page's apporach with listcomp

# n = 50

# factor = int(n / 5)

# li = [ [ 5*i + j for j in range(1, 6) ] for i in range(factor) ]

# print(li)



'''
  45. Write a Python program to convert a pair of values into a sorted unique array.

  input: [(1,2),(3,4),(1,2),(5,6),(7,8),(1,2),(3,4),(3,4),(7,8),(9,10)]
  output: [1,2,3,4,5,6,7,8,9,10]

'''

# inp = [(1,2),(3,4),(1,2),(5,6),(7,8),(1,2),(3,4),(3,4),(7,8),(9,1)]


# # My approach

# set1 = set()

# for i in inp:
    
#   for j in i:

#     set1.add(j)

# print(sorted(list(set1)))

''' ---------- '''

# #Page's approach with set unpacking

# print(sorted(set().union(*inp))) #They created a empty set and print the union with the unpacked list of tuples and then sorted.





'''
  281. Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list
  
    ([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
    ([0, -3, -5, -7, -8]) -> [[-3, 0], [-8, -5]]
    ([1, 2, 3, 4, 5]) -> [[1, 4], [2, 5]]
    ([100, 102, 103, 114, 115]) -> [[100, 103]]

'''

# li = [100, 102, 103, 114, 115]


''' ---------- '''

# # My listcomp approach

# res = [ [num1, num2] for num1 in li for num2 in li if abs(num1-num2) == 3 ]

# res = [ [ min(elem), max(elem)] for elem in res ]

# for i in res:
#   if res.count(i) > 1: res.remove(i)

# print(res)



''' ---------- '''

# # My approach

# res = []

# for i in li:
    
#   for j in li:

#     if abs(i - j) == 3: res.append(sorted([i,j]))

    
# for i in res:

#   if res.count(i) > 1: res.remove(i)

# print(res)


''' ---------- '''
    

# #Page's approach

# res = []

# for v, i in enumerate(li):
    
#   for j in li[ v+1 :]:

#     if abs(i-j) == 3: res.append([i,j])

# print(res)

# #Much more elegant




'''
  254.  Write a Python program to get the weighted average of two or more numbers
  
   Sample Output:
   
    Original list elements:
    [10, 50, 40]
    [2, 5, 3]
    Weighted average of the said two list of numbers:
    39.0

    Original list elements:
    [82, 90, 76, 83]
    [0.2, 0.35, 0.45, 32]
    
    Weighted average of the said two list of numbers:
    82.97272727272727

'''


li = [10, 50, 40]

w = [2, 5, 3]


''' ---------- '''



# # My approach with a function def

# def weight_average (li, w):

#   numerator = 0

#   for v, n in enumerate(li):
    
#     numerator += n * w[v]

#   result = numerator/sum(w)

#   return result

# print(weight_average(li, w))


''' ---------- '''


# # Another approach with zip, map and lambda functions

# res = list( zip( li, w ))

# avg = list( map( lambda x: x[0]*x[1], res ) )

# print(sum(avg)/sum(w))




'''
  279. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.

   Sample data :
   
    ([0, 3, 4, 7, 9]) -> False
    ([3, 5, 7, 13]) -> True
    ([1, 5, 3]) -> False

'''

# li =  [1, 5, 3]


# ''' ---------- '''


# cap = max(li)

# # primes generator

# def isprime (n, cap):

  # primes = []

  # non_primes = []

  # for i in range(2, cap+1):
    
  #   if i not in non_primes: 

  #     primes.append(i)

  #     for i in range(i*i, cap+1, i):

  #       non_primes.append(i)
  
#   if n in primes: return True
#   else: return False
  
  
# print( all( [ eval( f'isprime({i},{cap})') for i in li ] ) )

# print( ( [ eval( f'isprime({i},{cap})') for i in li ] ) ) 



  

'''
  280. Write a Python program to extract the first specified number of vowels from a given string. 
  If the specified number is less than number of vowels present in the string then display "n is less than number of vowels present in the string".

   Sample data :
   
    ("Python", 2) -> "n is less than number of vowels present in the string."
    ("Python Exercises", 3) -> "oEe"
    ("aeiou") -> "AEI"

'''


# n = 3

# s = 'Python'

# def vowelizer (s, n):

#   vowels = ''

#   for i in s:

#     if i in 'aeiouAEIOU': vowels += i

#   if len(vowels) < n: print('n is less than number of vowels present in the string')

#   else: print(vowels[:n]) 

# vowelizer('Python Exercises',n)




'''
  276.  Write a Python program to find the largest odd number in a given list of integers.

   Sample data :
   
    ([0, 9, 2, 4, 5, 6]) -> 9
    ([-4, 0, 6, 1, 0, 2]) -> 1
    ([1, 2, 3]) -> 3
    ([-4, 0, 5, 1, 0, 1]) -> 5

'''

# li = [1, 2, 3]

''' ---------- '''

# # Listcomp approach

# result = sorted( [ x for x in li if abs( x % 2 ) == 1 ], reverse = True)

# print(result[0])


''' ---------- '''

# # My original approach

# res = 0

# li = sorted(li, reverse = True)

# for i in li:

#   if i % 2 == 1: 

#     res = i

#     break

# print(i)




'''
  275. Write a Python program to add all elements of a list of integers except the number at index.

   Sample data :
   
    ([0, 9, 2, 4, 5, 6] -> [26, 17, 24, 22, 21, 20]
    ([-4, 0, 6, 1, 0, 2]) -> [9, 5, -1, 4, 5, 3]
    ([1, 2, 3]) -> [5, 4, 3]
    ([-4, 0, 5, 1, 0, 1]) -> [7, 3, -2, 2, 3, 2]

'''

# li = [-4, 0, 5, 1, 0, 1]

''' ---------- '''

# # My approach thru listcomps

# result = [ sum(li) - i for i in li ]

# print(result)

''' ---------- '''


# # My approach thru for loops

# res = []

# for v, n in enumerate(li):

#   res.append( sum(li) - li[v] ) 

# print(res)





'''
  267. Write a Python program to get the cumulative sum of the elements of a given list.

   Sample data :
   
    Original list elements:
    [1, 2, 3, 4]
    Cumulative sum of the elements of the said list:
    [1, 3, 6, 10]


    Original list elements:
    [-1, -2, -3, 4]
    Cumulative sum of the elements of the said list:
    [-1, -3, -6, -2]

'''


# li = [-1, -2, -3, 4]


# # My Fav Approach

# res = [ sum( li[:x+1] ) for x in range(len(li)) ] 

# print(res)


# # Another Approach

# res = []

# for v, n in enumerate(li):

#   res.append(sum(li[:v+1]))

# print(res)





'''
  265. Write a Python program to generate a list, containing the Fibonacci sequence, up until the nth term

    Sample Output:

    First 7 Fibonacci numbers:
    [0, 1, 1, 2, 3, 5, 8, 13]

    First 15 Fibonacci numbers:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]


'''

# # My approach with seeds

# li = [0, 1]

# n = 7

# for i in range(n-1):

#   li.append( li[i] + li[i+1] )

# print(li)





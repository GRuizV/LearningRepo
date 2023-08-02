import string
import math
import itertools
import random

'''
5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''

# # My solution

# def factorial(n = int):

#     if n == 0:

#         return 1
    
#     else:

#         res = 1

#         while n > 0:

#             res *= n

#             n -= 1

#         return res


# print(factorial(0))



'---------------'



# # Page's Solution

# def factorial(n):

#     if n == 0:

#         return 1
    
#     else:

#         return n * factorial(n-1)   #Solution with recursion


# print(factorial(5))





'''
7. Write a Python function that accepts a string and counts the number of upper and lower case letters. 

Sample String : 'The quick Brow Fox'

Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

'''



# # My solution

# def case_counter(s):

#     print( f'No. of Upper case characters : {len( [letter for letter in s if letter.isupper()] )}')
#     print( f'No. of Lower case characters : {len( [letter for letter in s if letter.islower()] )}') 
   


# string = 'The quick Brow Fox'

# case_counter(string)





'''
9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

'''

# #My solution

# def isprime(n):

#     primes = [1]
#     non_primes = []

#     for i in range(2, n+1):

#         if i not in non_primes:

#             primes.append(i)

#             for j in range(i*i, n+1, i):

#     if n in primes: 
#         print(f'{n} is a prime number')
    
#     else:
#         print(f'{n} is not a prime number')
   

# isprime(12)



'---------------'


# # Page's solution

# 'Direct comprobation'

# def isprime(n):

#     if n == 0:

#         return print('0 is a non prime number')

#     elif n == 1 or n == 2:

#        return print(f'{n} is a prime number')
            
#     else:

#         for i in range(2, n):
            
#             if n % i == 0:

#                 return print(f'{n} is non a prime number')


#     return print(f'{n} is a prime number')


# isprime(4)




'''
11. Write a Python function to check whether a number is "Perfect" or not. 

According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).

    Example : 

    The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
    Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

    The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

'''


# # My solution

# def isperfectnum(n):

#     divisors = [x for x in range(1, n) if n % x == 0]

#     if sum(divisors) == n: 

#         return True
        
#     return False




'''
12. Write a Python function that checks whether a passed string is a palindrome or not.

'''

# def ispalindrome(s):

#     if s == s[::-1]:

#         return print(f'{s} is a palindrome')
    
#     return print(f'{s} is not a palindrome')


# ispalindrome('madame')




'''
Pascal's Triangle

13. Write a Python function that prints out the first n rows of Pascal's triangle

    example:

    row 1:           [1]                                                        
    row 2:          [1,1]                
    row 3:         [1,2,1]                                                      
    row 4:        [1,3,3,1]              
    row 5:       [1,4,6,4,1]                                                    
    row 6:      [1,5,10,10,5,1]            
    row 7:     [1,6,15,20,15,6,1]                                              
    row 8:    [1,7,21,35,35,21,7,1]       
    row 9:   [1,8,28,56,70,56,28,8,1]                                           
    row 10: [1,9,36,84,126,126,84,36,9,1]


'''


# # My solution

# res = list()

# for i in range(1,11+1):

#     temp = list()

#     if i == 1:
#         res.append([1])

#     elif i == 2:
#         res.append([1,1])


#     elif i % 2 != 0:
        
#         for j in range(i//2):
#             temp.append( ( res[i-2][j] + res[i-2][j+1] ) )

#         # res.append( [1] + temp[:-1] + [temp[-1]] + list(reversed(temp[:-1]))  + [1] ) #this works
#         res.append( [1] + temp[:-1] + [temp[-1]] + temp[-2::-1]  + [1] ) #this works too
       
       
#     else:

#         for j in range(i//2-1):

#             temp.append( (res[i-2][j] + res[i-2][j+1]) )

#         res.append( [1] + temp + temp[::-1] + [1] )


# for i in res:
#     print(i)


'-----------'


#Pages solution

def pascal_triangle(n):
   
   trow = [1]

   y = [0]

   for x in range(max(n,0)):
      
      print(trow)

      trow=[l+r for l,r in zip(trow+y, y+trow)]

   return n>=1

pascal_triangle(6) 




'''
14. Write a Python function to check whether a string is a pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''


# # My solution

# def ispangram(s, alpha = string.ascii_lowercase):

#     test_string = ''.join(s.casefold().split())

#     test_string = ''.join(set(test_string))

#     return all([x in test_string for x in alpha ])


# tst_s = "The quick brown fox jumps over the lazy dog"

# print(ispangram(tst_s))


'---------------'



# # Page's Solution

# def ispangram(s, alpha = string.ascii_lowercase):

#     alpha_set = set(alpha)

#     return alpha_set <= set(s.lower())  #This was more elegant

# tst_s = "The quick brown fox jumps over the lazy dog"

# print(ispangram(tst_s)) 



''' ---------------------------------------------- '''








'''
EXERCISES FROM CODESOLID
'''




'''
1. Using a loop (that is, without using a slice), write a function “reverse_list” and takes a list as input 
and returns a copy of the list in which all the elements have been swapped (the first element with the last, the second with the next to last, etc.) 

input:

    [23, 4, 9, 6, 8, 22, 18]
    [6, 5, 2, 9, 44, 12]
    []

output:

    [18, 22, 8, 6, 9, 4, 23]
    [12, 44, 9, 2, 5, 6]
    []
'''


# def reverse_list(lst: list):

#     res = list()

#     for i in range(len(lst),0,-1):

#         res.append(lst[i-1])

#     return res

# l = [23, 4, 9, 6, 8, 22, 18]

# print(l)
# print(reverse_list(l))





'''
2. Write a function that takes in a string and returns the string with all the vowels
removed. Test it using the following code (you should see no output): 

Example

    remove_vowels("We all love Python!") == "W ll lv Pythn!"

'''


# def remove_vowels(s: str):

#     return ''.join([ x for x in s if x not in 'aeiouAEIOU' ])


# print(remove_vowels("We all love Python!"))





'''
3. Write a function that takes in a list of integers or floats and returns True if the list contains duplicates and False if the list does not contain duplicates.
Use a type hint to “enforce” the correct type.
'''

# def dupl_check(l:list):

#     if len(set(l)) == len(l):

#         return True
    
#     else:
        
#         return False
    

# print(dupl_check([1,2,3,4,5,8,0]))
# print(dupl_check([1,2,3,4,8,8]))





'''
6. Write a function with the following signature:

def display_box(width: int, height: int, character="*")
This function will draw a simple ASCII-art rectangle (non-filled) of the given height and width, 
using character to print the lines. 

For example, display_box(5, 4, 'x') should output the following:

xxxxx
x   x
x   x
xxxxx


'''

# def display_box(width: int, height: int, char="*"):

#     if width < 2 or height < 2:

#         raise Exception('neither dimention could be less than 2')
    
#     else:

#         for i in range(height):
            
#             if i == 0 or i == height-1:

#                 print(width*char) 

#             else:

#                 print(f'{char}{" "*(width-2)}{char}')

#         # [ print(width*char) if i == 0 or i == height-1 else print(f'{char}{" "*(width-2)}{char}') for i in range(height) ]

# display_box(5,4)





'''
7. This exercise is famous, and a perhaps one of the most popular “can you handle basic programming” interview questions. 

Write a function, fizzbuzz, with a single integer argument named value. If the value is evenly divisible by three, return the string “fizz”. 

It the value is evenly divisible by five, return the string “buzz”. If the value is evenly divisible by both three and five, return fizzbuzz. 

Finally, if none of these apply, return an empty string.


Test it with the following code:

values = [3,6,9,11,5,10,20,23,15,30,60]

for value in values:
    print(fizzbuzz(value))

'''

# def fizzbuzz(value):

#     if value %3 == 0 and value % 5 == 0:
#         return 'fizzbuzz'
    
#     elif value % 3 == 0:
#         return 'fizz'
    
#     elif value % 5 == 0:
#         return 'buzz'
  
#     else:
#         return ''



# values = [3,6,9,11,5,10,20,23,15,30,60]

# for value in values:
#     print(fizzbuzz(value)) 



''' ---------------------------------------------- '''








'''
Python Map - EXERCISES FROM W3Resource
'''




'''
2. Write a Python program to add three given lists using Python map and lambda.
'''

# l1 = [x for x in range(1,6)]
# l2 = [x for x in range(6,11)]
# l3 = [x for x in range(10,16)]

# print(l1, l2, l3)

# res = map( (lambda x, y, z: x + y + z) , l1, l2, l3)

# print(list(res))




'''
3. Write a Python program to listify the list of given strings individually 
using Python map.

Original list: 
['Red', 'Blue', 'Black', 'White', 'Pink']

After listify the list of strings are:
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

'''

# l1 = ['Red', 'Blue', 'Black', 'White', 'Pink']

# res = [x for x in map(list,l1)]

# print(res)




'''
6. Write a Python program to convert all the characters into uppercase and lowercase
and eliminate duplicate letters from a given sequence. 

Sample:
[a,B,d,D,e,F,g,T,Y,H,h,u,o,O]

'''

# li = ['a','B','d','D','e','F','g','T','Y','H','h','u','o','O']

# res = sorted({x for x in map(str.casefold, li)})

# res = [ (x.upper(), x.lower()) for x in res ]

# print(li)
# print(res)




'''
7. Write a Python program to add two given lists 
and find the difference between them. Use the map() function.

Original lists:
[6, 5, 3, 9]
[0, 1, 7, 7]

Result:
[(6, 6), (6, 4), (10, -4), (16, 2)]
'''

# l1 = [6, 5, 3, 9]
# l2 = [0, 1, 7, 7]

# res = [ ( x[0] + x[1], x[0] - x[1]) for x in map( (lambda x, y: (x, y)), l1, l2 ) ]

# print(res)




'''
9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
'''


# l = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'), ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]

# names = list(map(lambda x: x[0], l))
# bds = list(map(lambda x: x[1], l))
# weights = list(map(lambda x: int(x[2][:-2]), l))


# print(weights)




'''
10. Write a Python program to compute the square of the first N Fibonacci numbers, 
using the map function and generate a list of the numbers.
'''

# # My solution

# l1 = [0, 1]

# n = 10

# t = [ l1.append(l1[i-1] + l1[i]) for i in range(1, n+1)  ]

# res = list(map(lambda x: x**2, l1))

# print(l1)
# print(res)


'------------'


# Page's Solution


# def fibonnaci_nums(x=0, y=1):

#     yield x

#     while True:

#         yield y

#         x, y = y, x + y


# square = lambda x: x**2

# n = 10

# result = [x for x in map(square, itertools.islice(fibonnaci_nums(), n))]

# print(result)




'''
13. Write a Python program to count the same pair in two given lists. 

Original lists:
[1, 2, 3, 4, 5, 6, 7, 8]
[2, 2, 3, 1, 2, 6, 7, 9]

Number of same pair of the said two given lists:
4

'''

# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2 = [2, 2, 3, 1, 2, 6, 7, 9]

# d1 = { k:l1.count(k) for k in sorted(l1)}
# d2 = { k:l2.count(k) for k in sorted(l2)}

# res = 0

# for i in set(l1+l2):

#     if i in d1 and i in d2 and d1[i] > 0 and d2[i] > 0:
    
#         res += min(d1[i], d2[i])
       
# print(res)
































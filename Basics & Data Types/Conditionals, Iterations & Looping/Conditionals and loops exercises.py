import random
import string

'''
1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
'''

# res = list()

# for num in range(1500,2701):

#     if num % 7 == 0 and num % 5 == 0:

#         res.append(num)

# # Listcomp solution
# res = [x for x in range(1500,2701) if x % 7 == 0 and x % 5 == 0 ]

# print(len(res))





'''
2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit. 

[ Formula :  °F = (°C x 9/5) + 32  or °C = (°F - 32) x 5/9  ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius

'''


# temp_in = '60°C'

# temp_out = int()


# if 'c' in temp_in.lower():

#     temp_out = int( ''.join([x for x in temp_in if x.isnumeric()]) )

#     temp_out = (temp_out * (9/5) + 32)

#     print(f'{temp_in} is {temp_out:.0f} in Fahrenheit')


# else: 

#     temp_out = int( ''.join([x for x in temp_in if x.isnumeric()]) )

#     temp_out = (temp_out - 32) * (5/9)

#     print(f'{temp_in} is {temp_out:.0f} in Celsius')





'''
3. Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
on successful guess, user will get a "Well guessed!" message, and the program will exit.

'''


# num = random.randint(1, 9)

# guess = int()

# print(num)

# while num != guess :

#     guess = int(input('Guess the number:'))

#     if guess != num: 
        
#         print('Nope!')
#         print()


# print('Well guessed!')





'''
4. Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

'''


# n = 5 


'---------'


'My solution'

# for i in range(1, n+1):

#     print(i*'* ')

#     if i == n:

#         for j in reversed(range(1, i)):
            
#             print(j*'* ')
    

'---------'


'Pages Solution'

# for i in range(n):

#     for j in range(i):

#         print('* ', end='')
    
#     print()


# for i in range(n, 0, -1):

#     for j in range(i):

#         print('* ', end='')
    
#     print()





'''
6. Write a Python program to count the number of even and odd numbers in a series of numbers 

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :
Number of even numbers : 5
Number of odd numbers : 4

'''


# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# odds, even = list(), list()


# for i in nums:

#     if i%2 == 0: 
        
#         even.append(i)

#     else:

#         odds.append(i)


# print(f'Number of even numbers : {len(even)}')
# print(f'Number of even numbers : {len(odds)}')





'''
11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.

Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

'''


# rows = 3
# cols = 4

# res = list()

# for i in range(rows):

#     temp = list()

#     for j in range(cols):

#         temp.append(i*j)
    
#     res.append(temp)

# # #Listcomp solution
# # res =  [ [x*y  for x in range(cols)] for y in range(rows) ]

# print(res)





'''
15. Write a Python program to check the validity of passwords input by users. 

Validation :

At least 1 letter between [a-z] 
At least 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

'''

# import string

# pword = 'passwordW3r@100' 

# print(pword)


'-----------'

# # My solution

# low = [x for x in pword if x.islower()]
# upp = [x for x in pword if x.isupper()]
# num = [x for x in pword if x.isnumeric()]
# spc = [x for x in pword if x in string.punctuation]


# validation = [bool(x) for x in [low, upp, num, spc, len(pword) >= 6, len(pword) < 16 ]]


# if all(validation):

#     print('Safe Password')

# else:

#     print('Unsafe Password')


'-----------'

# # Pages Solution

# import re

# x = True

# while x:  

#     if (len(pword)<6 or len(pword)>16):
#         break

#     elif not re.search("[a-z]",pword):
#         break

#     elif not re.search("[0-9]",pword):
#         break

#     elif not re.search("[A-Z]",pword):
#         break

#     elif not re.search("[$#@]",pword):
#         break

#     elif re.search("\s",pword):
#         break

#     else:
#         print("Valid Password")

#         x=False

#         break

# if x:
#     print("Not a Valid Password")





'''
16. Write a Python program to find numbers between 100 and 400 (both included) 
where each digit of a number is an even number.
The numbers obtained should be printed in a comma-separated sequence. 

'''

# res = list()

# for num in range(100, 401):

#    if all( [ int(x)%2 == 0 for x in str(num) ] ):
      
#       res.append(num)


# print(res)





'''
17. Write a Python program to print the alphabet pattern 'A'.

Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *

'''


# c = '*'

# for row in range(8):

#     if row == 0:

#         print(f'{c*3:^5}')

#     if row == 1 or row == 2:

#         print(f'{c}{c*0:^3}{c}')
    
#     if row == 5:

#         print(f'{c*5}')

#     if row > 5:

#         print(f'{c}{c*0:^3}{c}')





'''
32. Write a Python program to check whether an alphabet is a vowel or consonant.

Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.

'''

# vowels = 'aeiouAEIOU'

# if input('Input a letter of the alphabet:') in vowels:

#     print('vowel')

# else:

#     print('consonant')





'''
41. Write a Python program to get the next day of a given date.
Expected Output:

Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23      

The next date is [yyyy-mm-dd] 2016-8-24 
'''

# import datetime

# 'The months having 31 days in a year: January, March, May, July, August, October, and December - [1,3,5,7,8,10,12]'


# year = 2000

# month = 1

# day = 28


# new_day, new_month, new_year = int(), int(), int()


# try: 
  
#   date = datetime.datetime(year,month,day)

#   if month in [1,3,5,7,8,10,12] and day == 30:
#     print(f'The next date is [yyyy-mm-dd]: {year}-{date:%m}-31')

#   elif abs(2000-year) % 4 == 0 and month == 2:
#     print(f'The next date is [yyyy-mm-dd]: {year}-{date:%m}-29')

#   elif month == 12 and day == 31:
#     print(f'The next date is [yyyy-mm-dd]: {year+1}-{datetime.datetime(year+1,1,1):%m}-01')

#   elif month in [1,3,5,7,8,10] and day == 31 or month in [4,6,9,11] and day == 30:
#     print(f'The next date is [yyyy-mm-dd]: {year}-{datetime.datetime(year,month+1,1):%m}-01')

#   elif month == 2 and day == 28:
#     print(f'The next date is [yyyy-mm-dd]: {year}-{datetime.datetime(year,month+1,1):%m}-01')

#   else: 
#     print(f'The next date is [yyyy-mm-dd]: {year}-{date:%m}-{day+1}')

# except ValueError: print('Enter a valid date!')





'''
42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
'''

# nums = list()

# while True:
    
#   inp = int( input('Next number:') )

#   if inp == 0:
#     break

#   nums.append(inp)

# print()
# print(f'The numbers list is: {nums}')
# print(f'The numbers sum is: {sum(nums)}')
# print(f'The numbers average is: {sum(nums)/len(nums)}')





'''
43. Write a Python program to create the multiplication table (from 1 to 10) of a number. 

Expected Output:

Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60 
'''

# num = 4

# res = [print(f'{num} x {i:<2} = {num*i:<2}') for i in range(1, 11)]





'''
44. Write a Python program to construct the following pattern, using a nested loop number. 

Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
'''


# res = [print(f'{i}'*i) for i in range(1,10)]













''' 
This series of excercises were taken from: https://www.w3resource.com/python-exercises/string/ 
'''
from timeit import default_timer as timer
import string


''' 
42. Write a Python program to count repeated characters in a string.

Sample string: 'thequickbrownfoxjumpsoverthelazydog'

Expected output :

o 4
e 3
u 2
h 2
r 2
t 2 


'''

# # Another Approach with sets and DictComp

# str1 = 'thequickbrownfoxjumpsoverthelazydog'

# set1 = set(str1)

# dict1 = dict()

# for i in set1:

#     dict1[i] = str1.count(i)


# dict1 = { k: v for k, v in sorted( dict1.items(), key = lambda x : x[1], reverse=True ) }

# print(dict1)


'''--------------'''


# #This is my approach based on string and list methods

# str1 = 'thequickbrownfoxjumpsoverthelazydog'

# list1 = []
# list2 = []

# for i in str1:

#     if i not in list1:

#        list1.append((i))

# for i in list1: list2.append(( i, str1.count(i) )) 

# list2 = sorted( list2, key=lambda x: x[1], reverse=True )


# print( list2 )



'''--------------'''


# #This the page approach based on dictionaries functionalities

# import collections

# d = collections.defaultdict(int)    #It'd be convinient to understand collections library

# str1 = 'thequickbrownfoxjumpsoverthelazydog'

# for i in str1:
#     d[i] += 1

# for i in sorted(d, key=d.get, reverse=True):
#   if d[i] > 1:
#       print('%s %d' % (i, d[i]))




''' 
43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.

Sample output:

The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3


'''

# #The solution is to use the '\u00b(x), where 'x' is the superscript'

# print('The area of the rectangle is 1256.66cm\u00b2')
# print('The volume of the cylinder is 1254.725cm\u00b3')



''' 
44. Write a Python program to print the index of the character in a string.

Sample string: w3resource

Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2

'''

# str1 = 'w3resource'

# for i in range(len(str1)):
#     print(f'Current character {str1[i]} position at {i}')




''' 
45. Write a Python program to check whether a string contains all letters of the alphabet.

'''

# import string

# # A more direct approach

# str1 = 'Write a Python program to check whether a string contains all letters of the alphabet.'
# # str1 = 'abcdefghijklmnopqrstuvwxyz'

# alph_letters = string.ascii_lowercase

# print(string.ascii_lowercase in str1.casefold())


'''----------------------'''

# # Initial Approach

# str1= 'w3resourceabcdefghijklmnopqrstuvwxyz'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# result = False  #This idea of initiation something in False and then turn it into True if a condition was not my idea, I think the while loop would work better

# for i in alphabet:
#     if i not in str1.casefold(): break
#     else: result = True 

# if result == True: print('The string contains all the letters in the alphabet')
# else: print('The string DOES NOT contain all the letters in the alphabet')




''' 
48. Write a Python program to swap comma and dot in a string. Go to the editor

Sample string: "32.054,23"
Expected Output: "32,054.23"

'''


# #There's actually a solution with makestrans & translate:

# trans_table = str.maketrans('.,',',.')

# str2 = str1.translate(trans_table)      #This is even more elegant and efficient

# print(str2)


'''----------------------'''

# str1 = '32.054,23'

# #With Slicing:
# comma = str1.find(',')

# dot = str1.find('.')

# str2 = str1[:dot]+str1[comma]+str1[dot+1:comma]+str1[dot]+str1[comma+1:]

# print(f'{str2}\n{str1}')


'''----------------------'''


# #With split() & join():

# str1 = ','.join(str1.split('.'))

# print('.'.join(str1.rsplit(',',1)))   #This one seems more elegant





''' 
49. Write a Python program to count and display the vowels of a given text

Sample output:

4                                                                                                             
['e', 'o', 'u', 'e']   

'''


# txt = 'A Write a Python program to count and display the vowels of a given text'

# txt = txt.casefold()

# list1 = [ x for x in txt if x in 'aeiou' ]

# print(f'{len(list1)}\n{list1}')



'''----------------------'''



# #The page approach:

# str1 = 'Write a Python program'

# def vowel(text):

#   vowels = "aeiuoAEIOU"

#   print(len([letter for letter in text if letter in vowels])) 
#   
#   print([letter for letter in text if letter in vowels])

# vowel(str1)





''' 
54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest. 

"abcbac"
"abcb"
"abcc"
"abcxxy"
"abc"

'''

# str1 = 'abcbac'

# str1 = str1.casefold()

# set1 = { x for x in str1 if str1.count(x) > 1 }

# list1 = list()

# for i in set1:

#     list1.append((i, str1.find(i, str1.find(i) + 1 )))

# list1 = sorted( list1, key = lambda x : x[1] ) 

# if len(list1) != 0: print (f'First repeated character: {list1[0][0]}\nNeareast repetition index: {list1[0][1]}')

# else: print('No repeated characters found')




''' 
56. Write a Python program to find the second most repeated word in a given string.

'''

# # With Sets & DictComp

# str1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I was not really happy'

# str1 = str1.casefold()

# words = set(str1.split())

# result = dict()


# for word in words:

#     result[word] = str1.split().count(word)


# result = { k: v for k, v in sorted( result.items(), key = lambda x: x[1], reverse = True ) if v > 1 }


# if len(result) > 1: print( f'The second most repeated word is "{list(result.keys())[1]}"\nIt appears {list(result.values())[1]} times in the string')

# else: print("There's not more than 1 repeated word in this string")




'''----------------------'''



#My approach based on string & lists methods

# str2 = "I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn't really happy"

# list1 = str2.casefold().replace('.','').split()


# count, list_word, list_rep, final_list = 0,[],[],[]


# for i in list1:

#     if list1.count(i) > 1:

#         if i in list_word: continue

#         else: list_word.append(i), list_rep.append(list1.count(i))  



# for i in range(len(list_word)): final_list.append((list_rep[i],list_word[i]))

# final_list = sorted(final_list, key=None, reverse= True)

# # print(final_list)

# if len(final_list) <= 1: print('There is no more than one repeated word in the string')
# else: print(final_list[1][1],final_list[1][0])



'''----------------------'''



# #The page approach:


# str2 = "I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn't really happy"


# def word_count(str):

#     counts = dict()
#     words = str.split()

#     for word in words:

#         if word in counts:

#             counts[word] += 1

#         else:

#             counts[word] = 1


#     counts_x = sorted(counts.items(), key=lambda v: v[1])
   
#     print(counts_x)

#     return counts_x[-2]


# print(word_count(str2))


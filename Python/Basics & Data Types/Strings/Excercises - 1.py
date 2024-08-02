''' 
This series of excercises were taken from: https://www.w3resource.com/python-exercises/string/ 
'''

from timeit import default_timer as timer


''' 1. Write a Python program to calculate the length of a string '''

# print('Hi, type anyhting, I will tell you the lenght of what you typed:   ')

# my_string = input()

# print(len(my_string))

## DONE



''' 
2. Write a Python program to count the number of characters (character frequency) in a string 

Sample String : 'google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1} 

'''

# # Set Approach

# s = 'google.com'

# set1 = set(s)

# result = []

# for i in set1:

#     result.append(f'{i}: {s.count(i)}')

# print(result)


'''---------------------'''


# # Dictionary Approach


# s = 'google.com'

# result = dict()

# for i in s:

#     if i in result: result[i] += 1

#     else:   result[i] = 1

# # result = dict( sorted(result.items(), key= lambda x: x[1], reverse= True) )   # The dict typed needed to be cast since sorte() returns a list.

# result = { k: v for k, v in sorted(result.items()) }    # DictComp makes it even easier, this way is sorted by key.
# result = { k: v for k, v in sorted(result.items(), key= lambda v: v[1], reverse=True ) }    # This DictComp sort by value.

# print(result)



'''---------------------'''


# # First Approach


# my_string = 'google.com'

# char_letter = []         # I first create a list to store each letter of the string


# for i in my_string:

#     if i in char_letter:

#         continue

#     else:

#         char_letter.append(i)


# str_counter = 0

# char_number = []

# for i in char_letter:       # Second, I create a list to store how many time does the letter appears in the string

#     str_counter = my_string.count(i)

#     char_number.append(str_counter)


# final_list = []

# for i in range(len((char_letter))):        # Third, I join each respective letter with its frequency (number)

#     final_list.append(f" '{char_letter[i]}': {char_number[i]}")
    

# final_str = '{'+ f"{','.join(final_list)}"+ '}' 

# print(final_str)





''' 
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.  

Sample String : 'w3resource'
Expected Result : 'w3ce'

Sample String : 'w3'
Expected Result : 'w3w3'

Sample String : ' w'
Expected Result : Empty String

'''

# print('Type something:   ')

# new_string = input()

# if len(new_string) < 2:

#     print('Empty String')

# else:

#     print(f'{new_string[:2]}{new_string[-2:]}')

# DONE



''' 
4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char.

Sample String : 'restart'
Expected Result : 'resta$t'

'''


# # Original Approach

# new_string = 'restarter'

# print(f"{new_string[0]}{new_string[1:].replace(new_string[0],'$')}")    # One-liner solution.




''' 
5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string 

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

'''

# print('Type something:')

# str1 = input()

# print('Now, the second string:')

# str2 = input()

# print(f'{str2[0:2]}{str1[2:]} {str1[0:2]}{str2[2:]}') 




''' 
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged. 

Sample String : 'abc'
Expected Result : 'abcing'

Sample String : 'string'
Expected Result : 'stringly'

'''


# str1 = 'abcing'


# if len(str1) <3:
#     print(str1)

# elif str1[-3:] == 'ing':
#     print(f"{str1}ly")

# else:
#     print(f"{str1}ing")





''' 
7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

Sample String : 'The lyrics are not that poor!'
Expected Result : 'The lyrics are good!'

Sample String : 'The lyrics are poor!'
Expected Result : 'The lyrics are poor!'

'''


# str1 = 'The lyrics are not even so that poor!'


# # if str1.find('not') != -1 and str1.find('poor') != -1 and str1.find('not') < str1.find('poor'):

# #     print( str1.replace( str1[ str1.find('not') : str1.find('poor') + 4 ], 'good' ))


# if 'not' in str1 and 'poor' in str1 and str1.find('not') < str1.find('poor'):

#     print( str1.replace( str1[ str1.find('not') : str1.find('poor') + 4 ], 'good' ))


# else: print (str1)





''' 
8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

Sample Output:
Longest word: Exercises
Length of the longest word: 9

'''

# # Sort approach

# list1 = ['Longest', 'Exercises' , 'Space' , 'Length' , 'Separate' ]

# list1.sort(key = len, reverse=True )

# print(f'{list1[0]} : {len(list1[0])}' )


'''--------------'''

# # My first approach.
 
# list1 = ['Longest', 'Exercises' , 'Space' , 'Length' , 'Separate' ]

# len1 = 0

# str1 = ''

# for i in list1:
    
#     if len1 < len(i):

#         str1 = i 
        
#         len1 = len(i) 
    
# print(f'Longest word: {str1}\nLength of the longest word: {len1}')




''' 
9. Write a Python program to remove the nth index character from a nonempty string.

'''

# print('Type something:')

# str1 = input()

# print('Type the index of the character to be removed:')

# index = int(input())

# print(f'{str1[:index]}{str1[index+1:]}')





''' 
10.  Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

'''

# print('Type something:')

# str1 = input()

# print(f'{str1[-1]}{str1[1:-1]}{str1[0]}')





''' 
11.  Write a Python program to remove the characters which have odd index values of a given string.

'''

# str1 = 'Write a Python program to remove the characters which have odd index values of a given string'

# str2 = ''

# for i in range(len(str1)):

#     if i%2 == 0: str2 += str1[i]

# print(str2)




''' 
12.  Write a Python program to count the occurrences of each word in a given sentence.

'''

# # With a set and dictionary

# str1 = 'my sad little bycicle is not my little sad bycicle anymore'

# set1 = set(str1.split())

# dict1 = dict()

# for i in set1:

#     dict1[i] = str1.split().count(i)

# dict1 = { k: v for k,v in sorted( dict1.items(), key= lambda x: x[1], reverse=True ) }

# print(dict1)



'''--------------'''


# # My first approach was a list of tuples

# str1 = 'my sad little bycicle is not my little sad bycicle anymore'.split()

# count = 0

# list1 = []
# list2 = []

# for i in str1:

#     if i not in list1:          # the 'not in' is new to me

#         list1.append(i)
#         count = str1.count(i)
#         list2.append((i,count))


# for i in range(len(list2)):

#     print(f"word '{list2[i][0]}' - count: {list2[i][1]}")



'''--------------'''


# # The page approach: A dictionary  // To my liking this is more efficient

# counts = dict()

# words = 'my sad little bycicle is not my little sad bycicle anymore'.split()

# for i in words:

#     if i in counts:
#         counts[i] += 1

#     else:
#         counts[i] = 1

# print(counts)




''' 
15.  Write a Python function to create the HTML string with tags around the word(s)

Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

'''

# def add_tags(tag, text):

#     return f"<{tag}>{text}</{tag}>"

# input_text = input('Which text would you like to be tagged:')

# input_tag = input('Which tag would you like to be wrap the text:')

# print(add_tags(input_tag, input_text))



''' 
19.  Write a Python program to get the last part of a string before a specified character

'''

# #My approach:

# input_text = 'https://www.w3resource.com/python-exercises/string'

# input_char = '-'

# if input_text.find(input_char) != -1: index = input_text.find(input_char)
# else: print('Character not found!')

# print(f'{input_text[0:index]}')



'''--------------'''



# #The page approach is way efficent

# str1 = 'https://www.w3resource.com/python-exercises/string'

# print(str1.rsplit('/', 1)[0])

# print(str1.rsplit('-', 1)[0])




''' 
20.  Write a Python function to reverse a string if it's length is a multiple of 4

'''

# txt = "Write a Python function to reverse a string if it's length is a multiple of 4   "

# if len(txt) % 4 == 0: print(txt[::-1])

# else: print('Not multiple of 4')




''' 
21.  Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters

'''

# # ListComp Approach

# txt = 'WRite a Python function to convert a given string to all uppercase if it contains' 

# if len([ x for x in list(txt)[:4] if x.isupper()]) >= 2 :    print(txt.upper())

# else:   print("There's not 2 uppercased letters in the first 4 characters of the string") 




'''--------------'''



# # Initial Approach

# txt = 'Write a Python function to convert a given string to all uppercase if it contains' 

# count = 0

# for i in txt[:4]:

#     if i.isupper(): count += 1
    
# if count >= 2: print(txt.upper())
# else: print('There is not at least 2 uppercases in the first 4 characters') 





''' 
25.  Write a Python program to create a Caesar encryption.

Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
The method is named after Julius Caesar, who used it in his private correspondence.

'''

import string


# base1 = string.ascii_letters

# number = int(input('insert the shift:'))

# number %= 56

# base2 = base1[ -number : ] + base1[ 0 : -number ]

# trans_table = str.maketrans(base1, base2)

# str1 = input('\nWhat word should be translated:')

# str2 = str1.translate(trans_table)

# print(f"\nthe encrypted word would be '{str2}'")


'''--------------'''


# # New attempt to make a decryption without looking the previous work / Feb '23

# decrypt_key = int(input('\nWhats the decryption key:'))

# decrypt_key = decrypt_key % 56

# base3 = base1[ -decrypt_key : ] + base1[ : -decrypt_key]

# trans_table2 = str.maketrans(base3,base1)

# str3 = input('\nWhats the word encrypted:')

# str4 = str3.translate(trans_table2)

# print(f"\nthe decrypted word would be '{str4}'")




'''--------------'''


# #This is the decryption of the caesar's encryption

# decrypt_key = int(input('\nto decrypt intsert the original shift:'))

# decrypt_key %= 52

# decrypt_key = 52 - decrypt_key

# base3 = base2[-decrypt_key:] + base2[0:-decrypt_key]

# trans_table= str.maketrans(base2,base3)

# str3 = str2.translate(trans_table)

# print(f"\nthe decrypted word would be '{str3}'")



'''--------------'''



# # #This how NeuralNine resolved this problem creating a function, link:https://www.youtube.com/watch?v=JEsUlx0Ps9k

# def caesar(text, shift, alphabets):

#     def alphabet_shifter(alphabet):

#         return alphabet[-shift:] + alphabet[:-shift]

#     shifted_alphabets = tuple( map( alphabet_shifter, alphabets ))

#     final_alphabet = ''.join(alphabets)

#     final_shifted_alphabet = ''.join(shifted_alphabets)

#     table = str.maketrans( final_alphabet, final_shifted_alphabet)

#     return text.translate(table)

# input_text = input('Type here the text to be encrypted:')
# input_shift = int(input('Type here the shift for the encryption:'))

# print(f"\nThe text encrypted is '{caesar(input_text,input_shift,[string.ascii_lowercase])}'")       #if I include string.ascii_uppercase, string.punctuation it would consider all those characters






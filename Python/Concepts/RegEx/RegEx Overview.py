import re


'Corey Schafer CheatSheet'

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group


# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )


# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+


"   Corey's Example: emails"

# emails = '''
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafer@my-work.net
# '''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)



"   Corey's Example: urls"

# urls = '''
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov
# '''

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))




"   Corey's practical case"

text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat, mat, pat, bat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''

# urls  = '''
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov
# '''

# # Pattern to match ...
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# subbed_urls = pattern.sub(r'\2\3', urls)   # within the subbed function the backslashed numbers are called "Back references"
# print(subbed_urls)

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match.group(3))



# Pattern to match emails
# pattern = re.compile(r'[A-Za-z.-_0-9]+@[A-Za-z-]+\.(com|net|edu)')

# # Pattern to match Mr., Mr, Ms, Ms., Mrs. and Mrs
# pattern = re.compile(r'M[rs]+\.?\s[A-Z]\w*')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # The same but working with groups '(...)'
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # The same but more legible

# # Pattern to match any number with dash or dot as sep.
# pattern = re.compile(r'\d+[-.]\d+[-.]\d+')

# # Pattern to match any number that starts with 900 or 800
# pattern = re.compile(r'[89]00+[-.]\d+[-.]\d+')





# #   working with a plain-text file and string parsing
# with open(r'C:\Users\USUARIO\GR\Software Development\Learning\Concepts\RegEx\data.txt', 'r') as f:

#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)






'The re module'

# #   The re.compile func

# email_pattern = re.compile(r'\w+@\w+\.\w+')

# text = "Contact us at email@example.com or support@example.org for assistance."

# matches = email_pattern.findall(text)

# print(matches)  # ['email@example.com', 'support@example.org']




# #   The re.search func

# pattern = re.compile(r'fox')

# text = "The quick brown fox jumps over the lazy dog"

# match = pattern.search(text)

# print(match)  # <re.Match object; span=(16, 19), match='fox'> / A regex object

# print(match.group())    # fox / The actual matched string


# #       groups matters not only to prinout readable strings, but to select each individual group specified in the pattern.

# pattern = re.compile(r'(\w+) (\w+) (\w+)')

# text = "The quick brown fox jumps over the lazy fox, while a group of foxes watched"

# match = pattern.search(text)

# print(match.group())    # The quick brown

# print(match.group(1))   # the
# print(match.group(2))   # quick
# print(match.group(3))   # brown




# #   The re.findall func

# text = "The quick brown fox jumps over the lazy dog with another fox"

# matches = re.findall(r'fox', text)

# print(matches)  # Output: ['fox', 'fox']




# #   The re.sub func

# text = "The quick brown fox jumps over the lazy dog with another fox"

# new_text = re.sub(r'fox', 'cat', text)

# print(new_text)  # Output: The quick brown cat jumps over the lazy dog with another cat


# new_text = re.sub(r'fox', 'cat', text, count=1)

# print(new_text)  # Output: The quick brown cat jumps over the lazy dog with another fox




# #   The re.split func

# text = "The quick brown fox jumps over the lazy dog"

# splitted_text = re.split(r'o', text)

# print(splitted_text)  # Output: ['The quick br', 'wn f', 'x jumps ', 'ver the lazy d', 'g']




'   RegEx Flags'

# text = "The quick brown fox\nJumps over the lazy dog"

# # Case-insensitive search
# pattern = re.compile(r'fox', re.IGNORECASE)
# match = pattern.search(text)

# if match:
#     print("Pattern found:", match.group())  # Pattern found: fox

# # Multiline search
# pattern = re.compile(r'^Jumps', re.MULTILINE)
# match = pattern.search(text)

# if match:
#     print("Pattern found at the start of a line:", match.group())   # Pattern found at the start of a line: Jumps 

# # Dotall search
# pattern = re.compile(r'brown.*dog', re.DOTALL)
# match = pattern.search(text)

# if match:
#     print("Pattern found across multiple lines:", match.group())    # Pattern found across multiple lines: brown fox
# # Jumps over the lazy dog

# # Verbose pattern
# pattern = re.compile(r'''
#     \b  # Word boundary
#     the  # Match 'the'
#     \b  # Word boundary
# ''', re.VERBOSE)
# match = pattern.search(text)

# if match:
#     print("Pattern found using verbose pattern:", match.group())    # Pattern found using verbose pattern: the 






'Basic Example'

# str = 'an example word:cat!!'

# match = re.search(r'word:\w\w\w', str)

# if match:
#     print('found', match.group())   # printout: found word:cat

# else:
#     print('No occurrences found')






'Literals Matching Example'

# # without case sensitivity
# txt = "Hello there! This is a hello message."
# pattern = r'hello'

# match = re.findall(pattern, txt, flags=re.IGNORECASE)


# if match:
#     print('found:', match)   # printout - found: ['Hello', 'hello']

# else:
#     print('No occurrences found')


# # with case sensitivity
# txt = "Hello there! This is a hello message."
# pattern = r'hello'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: ['hello']

# else:
#     print('No occurrences found')




# # period matching
# txt = "Hello there. New message."
# pattern = r'\.'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: ['.', '.']

# else:
#     print('No occurrences found')




# # whitespace matching
# txt = "Hello there. New message."
# pattern = r'\s'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: [' ', ' ', ' ']

# else:
#     print('No occurrences found')
    



# # newline matching
# txt = '''Hello there.
# New message.'''

# pattern = r'\n'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: [' ', ' ', ' ']

# else:
#     print('No occurrences found')



'   Other basic patterns'


# # letter, digits and underscore matching

# txt = '''Hello there, again. 15 New messages!'''

# pattern = r'\w'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: ['H', 'e', 'l', 'l', 'o', 't', 'h', 'e', 'r', 'e', 'a', 'g', 'a', 'i', 'n', '1', '5', 'N', 'e', 'w', 'm', 'e', 's', 's', 'a', 'g', 'e', 's']

# else:
#     print('No occurrences found')




# # word boundary

# txt = '''Hello there, again. 15 New messages!'''

# pattern = r'\bagain\b'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: ['again']

# else:
#     print('No occurrences found')




# # digits

# txt = '''Hello there, again. 15 New messages!'''

# pattern = r'\d+'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: ['15']

# else:
#     print('No occurrences found')






'Metacharacter patterns'

# # dot '.'

# txt = '''Hello there, again. 15 New messages!'''

# pattern = r'e.'

# match = re.findall(pattern, txt)


# if match:
#     print('found:', match)   # printout - found: ['el', 'er', 'e,', 'ew', 'es', 'es']

# else:
#     print('No occurrences found')




# # Carret '^' and Dollar '$'

# pattern_start = r'^hello'
# pattern_end = r'end$'

# text = "hello there, end"

# match_start = re.findall(pattern_start, text)
# match_end = re.findall(pattern_end, text)

# print(match_start)  # Output: ['hello']
# print(match_end)    # Output: ['end']




# # Backslash '\'

# pattern = r'\.'

# text = "A period. Not the end."

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['.', '.']




# # Pipe '|'

# pattern = r'cat|dog'
# text = "I have a cat and a dog. and you know what? another dog too"

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['cat', 'dog', 'dog']






'Quantifiers'

# # Asterisk
# pattern = r'ab*'  # Matches 'a' followed by zero or more 'b's

# text = "ac abb abbb abc"

# matches = re.findall(pattern, text)
# print(matches)  # Output: ['a', 'abb', 'abbb', 'ab']



# pattern = r'\bre\w*ing\b'
# text = "Reading is refreshing. The red car is racing."

# matches = re.findall(pattern, text, flags=re.IGNORECASE)
# print(matches)  # Output: ['Reading', 'refreshing']




# # Plus
# pattern = r'ab+'  # Matches 'a' followed by one or more 'b's

# text = "ac abb abbb abc"

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['abb', 'abbb', 'ab']




# # Question Mark
# pattern = r'colou?r'  # Matches 'colour' or 'color'

# text = "The colour of the car is blue, but color is also acceptable."

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['colour', 'color']




# # Curly braces
# pattern = r'a{2}'  # Matches with anything with 2 consecutive (a)s

# text = "a aa aaa aaaa aaaaaa abaa ava aara"

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa']


# pattern = r'a{1,3}'  # It also matches with inclusive ranges of (a)s

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['a', 'aa', 'aaa', 'aaa', 'a', 'aaa', 'aaa', 'a', 'aa', 'a', 'a', 'aa', 'a']


# pattern = r'a{3,}'  # and lastly It'll also match with values higher than n {n,}

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['aaa', 'aaaa', 'aaaaaa']


# pattern = r'a{1,2}|a{0}'  # Since maximal count is not suported {,n}, the pattern that will suffice for this is this one, for up to 2 count

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['a', '', 'aa', '', 'aa', 'a', '', 'aa', 'aa', '', 'aa', 'aa', 'aa', '', 'a', '', 'aa', '', 'a', '', 'a', '', 'aa', '', 'a', '']






'Charater Classes'

# # [aeiou] 
# pattern = r'[aeiou]'  # Matches with any vowel

# text = "The Price is $20."

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['e', 'i', 'e', 'i']


# # [A-Z] 
# pattern = r'[A-Z]'  # Matches with any Uppercased letter

# text = "The Price is $20."

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['T', 'P']


# # [A-Za-z] 
# pattern = r'[A-Za-z]'  # Matches with any Uppercased or lowercased letter

# text = "The Price is $20."

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['T', 'h', 'e', 'P', 'r', 'i', 'c', 'e', 'i', 's']


# # [0-9] 
# pattern = r'[0-9]'  # Matches with any digit

# text = "The Price is $20."

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['2', '0']


# # [^0-9] 
# pattern = r'[^0-9]'  # Matches with anything but a digit

# text = "The Price is $20."

# matches = re.findall(pattern, text)

# print(matches)  # Output: ['T', 'h', 'e', ' ', 'P', 'r', 'i', 'c', 'e', ' ', 'i', 's', ' ', '$', '.']


'   practical cases'
# # Practical case: Matches with words only composed by vowels
# pattern = r'\b[aeiou]+\b'  # Matches with words only made by vowels

# text = "aea apple tree juice oui"

# matches = re.findall(pattern, text, flags=re.IGNORECASE)

# print(matches) # ['aea', 'oui']

# #   Practical case: Matches with words that contains two vowels adjacent
# pattern = r'\b\w*?[aeiou]{2}\w*?\b'

# text = "aea apple tree juice oui"

# matches = re.findall(pattern, text, flags=re.IGNORECASE)

# print(matches) # ['aea', 'tree', 'juice', 'oui']

# #   Practical case: Matches with words that starts with two adjacent vowels
# pattern = r'\b[aeiou]{2}\w*?\b'

# text = "aea apple tree juice oui"

# matches = re.findall(pattern, text, flags=re.IGNORECASE)

# print(matches) # ['aea', 'tree', 'juice', 'oui']










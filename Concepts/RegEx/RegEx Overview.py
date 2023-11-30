import re


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




# Question Mark
pattern = r'colou?r'  # Matches 'colour' or 'color'

text = "The colour of the car is blue, but color is also acceptable."

matches = re.findall(pattern, text)

print(matches)  # Output: ['colour', 'color']



























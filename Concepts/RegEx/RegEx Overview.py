import re


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



# dot '.'

txt = '''Hello there, again. 15 New messages!'''

pattern = r'e.'

match = re.findall(pattern, txt)


if match:
    print('found:', match)   # printout - found: ['el', 'er', 'e,', 'ew', 'es', 'es']

else:
    print('No occurrences found')
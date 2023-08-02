
# num = ' 2'

# num = int(num)

# print(num*10)

# # Output: 107
# print(0b1101011)

# # Output: 253 (251 + 2)
# print(0xFB + 0b10)

# # Output: 13
# print(0o15)


'''
math, fractions and random built-in modules

'''

import math, fractions

# print(math.pi)

# print(math.pi)

# print(math.cos(math.pi))

# print(math.exp(10))

# print(math.log10(1000))

# print(math.sinh(1))

# print(math.factorial(6))


import random
from statistics import geometric_mean, mean
from unicodedata import decimal
from unittest.util import sorted_list_difference


# print(random.randrange(10, 20))

# x = ['a', 'b', 'c', 'd', 'e']

# # Get random choice
# print(random.choice(x))

# # Shuffle x
# random.shuffle(x)

# # Print the shuffled x
# print(x)

# # Print random element
# print(random.random())



'''
bult-in sum() functions vs for loop
'''

from timeit import default_timer as timer

# c = 0

# start = timer()

# for i in range (30000000):
#     c += i

# stop = timer()

# print(f'Result: {c:,}\nTime: {stop-start}')



# start = timer()

# s = sum(range (30000000))

# stop = timer()


# print(f'Result: {s:,}\nTime: {stop-start}')


'''-------------'''



'''

list(range(x)) vs listcomp

'''

# start = timer()

# print( list(range(53)) )

# end = timer()

# print( end - start )


# start = timer()

# print( [ x for x in range(53)] )

# end = timer()

# print( end - start )


'''-------------'''



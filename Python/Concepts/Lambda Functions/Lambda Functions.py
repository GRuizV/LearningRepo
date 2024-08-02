
'''
Lambdas could be staded directly: (lambda x: x+1)(2), would be 
the same as passing '2' to the function.

    btw: this kind of statements (lambda x: x+1)(2) 
    are called IIFE or Iffy meaning "Immediately Invoked Function Expression" 

'''
# print((lambda x: x+1)(2))



'''Lambdas could also take multiple arguments: lambda x, y: x + y'''

# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# print(full_name('gerardo', 'ruiz')) # Full name: Gerardo Ruiz



'''Lambdas could be Higher-oerder Functions, meaning: receive funcs as arguments'''

# high_ord_func = lambda x, func: x + func(x)

# print(high_ord_func(2, lambda x: x*x))   # 6
# print(high_ord_func(3, lambda x: x + 1))   # 7



'''Lambdas does not support statements aside if-else'''

# (lambda x: assert x == 2)(2)    # SyntaxError: invalid syntax

# print((lambda x: 'Even' if x%2 == 0 else 'Odd')(2)) # Even

'   It could even have nested ifs, but if thats the case itd be better to call an actual function'

# print((lambda x: 'A' if x > 10 else ('B' if x > 5 else 'C'))(2)) # C
# print((lambda x: 'A' if x > 10 else ('B' if x > 5 else 'C'))(11)) # A
# print((lambda x: 'A' if x > 10 else ('B' if x > 5 else 'C'))(8)) # B



'''Lambdas support various types of parameters '''

# # Positional arguments
# print((lambda x, y, z: x + y + z)(1, 2, 3)) # 6

# # Named arguments
# print((lambda x, y, z=3: x + y + z)(1, 2)) # 6

# # Named & Defined arguments
# print((lambda x, y, z=3: x + y + z)(1, y=2)) # 6

# # Arbitrary arguments
# print((lambda *args: sum(args))(1, 2, 3)) # 6

# # Keyword arguments
# print((lambda **kwargs: sum(kwargs.values()))(one = 1, two = 2, three = 3)) # 6

# # Default arguments
# print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)) # 6



'''Lambdas can be tested with unittest'''

# import unittest

# addtwo = lambda x: x + 2

# class LambdaTest(unittest.TestCase):
#     def test_add_two(self):
#         self.assertEqual(addtwo(2), 4)

#     def test_add_two_point_two(self):
#         self.assertEqual(addtwo(2.2), 4.2)

#     def test_add_three(self):
#         # Should fail
#         self.assertEqual(addtwo(3), 6)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)



'''Classic Functional Constructs with Lambdas'''

# # with map
# print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))    # ['CAT', 'DOG', 'COW']

# # with filter
# print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow'])))  # ['dog', 'cow']

# # with reduce
# from functools import reduce
# print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow']))  # cat | dog | cow



'''Lambdas in Key Functions'''

# ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
# print(sorted(ids)) # Lexicographic sort: ['id1', 'id100', 'id2', 'id22', 'id3', 'id30']

# sorted_ids = sorted(ids, key=lambda x: int(x[2:])) 
# print(sorted_ids)   # Integer sort: ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

# ''' Same works for list.sort(), min(), max() & others...'''



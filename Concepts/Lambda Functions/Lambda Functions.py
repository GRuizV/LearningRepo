
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










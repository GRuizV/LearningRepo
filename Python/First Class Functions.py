
from cmath import sqrt
import math


# def square(x):
#     return x * x

# f = square

# def my_map(func, argm_list):
#     result = []

#     for i in argm_list:
#         result.append(func(i))

#     return result

# new_list = my_map(math.sqrt,[1,2,3,4,5])


# print(new_list)


''' 

This was just me playing to try to build my own cube maker 
based on the square function created below
    
'''

# def cube (func):

#     base = int(math.sqrt(func))

#     result = base * func
    
#     return result

# new_cube = cube(square(5))

# print (new_cube)



''' 

To better understand FC_functions and Higher order functions, next, the logger example:
Here is show how after having a function that has a function inside it would serve
as a function converter to any variable.

'''

def logger (msg):

    def log_message ():

        print('Log:',msg)
    
    return log_message

hi_msg = logger

new_hi_msg = hi_msg('Hey there!')

new_hi_msg()


'''
And finally, a more practical example of higher order functions.

A text wrapper

'''

# def html_tag(tag):

#     def text_wrap(msg):

#        print(f'<{tag}>{msg}</{tag}>') 
    
#     return text_wrap

# print_h1 = html_tag('h1')

# print_h1('Headline')

# print_h1('Another Headline')


# print_p = html_tag('p')

# print_p('Paragraph')



























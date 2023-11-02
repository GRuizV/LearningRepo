
# def hello_func():
#     return 'Hello Function'

# print(hello_func().upper())




# def hello_func(name='You', greeting,):

#     return f'{greeting}, {name}!'


# print(hello_func(name = 'me', 'Hey'))




'Positional Arguments'

# def info(name, age):

#     print(f'Hi, my name is {name} and I am {age} years old')

# info('Tom', 24)




# def info(name, age=24):

#     print(f'Hi, my name is {name} and I am {age} years old')

# info(age=25, 'Tom')




'Arbitrary Arguments (*Args)'

# def my_func(*args):

#     for i in args:

#         print(i)


# my_func(1, 'a', (None, None), {1,3,5})




'Keyword and Default Arguments'

# 'Keyword'
# def my_func(greeting=str, name=str, city=str):

#     print(f'{greeting} {name} from {city}!')


# my_func()

# my_func(greeting='Hello', name='Tom', city='Orlando')


# 'Default'
# def my_func(greeting='Hi', name='Jerry', city='NY'):

#     print(f'{greeting} {name} from {city}!')


# my_func()

# my_func(greeting='Hello')




'Arbitrary Keyword Arguments (**Kwargs)'

# '**kwargs'
# def my_func(**kwargs):

#     for k, v in kwargs.items():

#         print(f'"{k}" is the key and "{v}" is the value')


# my_func( shoes = 'Adidas', shirt = 'H&M', socks = 'Nike')




'kwarg and **kwargs combined'

# def my_func(greeting='hi', name = "Ken", **kwargs):

#     for k, v in kwargs.items():

#         print(f'{greeting} {name}, your {k} are from the "{v}" brand')


# my_func( shoes = 'Adidas', shirt = 'H&M', socks = 'Nike')




'Function with all kind of arguments'

# def my_func(name, lastname, *args, greeting=str, treatment = "Mr.", **kwargs):

#     print(f'''{greeting}, {treatment} {name} {lastname}!
    
#     At the moment you posses {[x for x in args]} in your account

#     and { {k:v for k,v in kwargs.items()} } in your stock
    
#     ''')


# account = ['$1000 COP', '$2500 USD', '$51000 RBL']

# stock = {'horses' : 4, 'boats' : 10, 'cars' : 1}

# my_func('Thomas', 'Shelby', *account , greeting='Good Evening', **stock)




'another example'


# def my_func(*kids, **courses_grades):
#     '''This is the docstring of this function'''

#     for kid in kids:

#         for c, g in courses_grades.items():

#             print(f'{kid} - {c}: {g}')


# # my_func('Tom', 'Susan', 'Nate', 'Sarah', spanish = 5, compsci = 9, math = 10 )

# print(my_func.__doc__)






'''

VARIABLES

    Global, Local and Nonlocal

'''



'Global'

# x = 'Global'

# def func():

#     global x

#     y = 'Local'

#     x = x * 2

#     print(x)

#     print(y)


# print('Global x =', x)

# func()

# print('Global x =', x)




'local'

# x = 5

# def func():

#    x = 10

#    print('Local x =', x)


# print('Global x =', x)

# func()

# print('Global x =', x)




'Nonlocal'


# def outer():

#     x = 'local'

#     def inner():

#         # nonlocal x

#         x = 'nonlocal'

#         print('inner: ', x)
    
#     inner()

#     print('outer: ', x)



# outer()
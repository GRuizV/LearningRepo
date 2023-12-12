from timeit import default_timer as timer
import time 
import functools


"First... Closures"

# def outer_function(x):

#     def inner_function(y):
    
#         return x + y
    
#     return inner_function

# closure_example = outer_function(5)

# result = closure_example(3)

# print(result)






'Now, an actual decorator'

# def log_function(func):

#     def wrapper(*args, **kwargs):

#         print(f'Calling {func.__name__} with args: {args} and kwargs: {kwargs}')

#         return(func(*args, **kwargs))
    
#     return wrapper


# @log_function
# def greet(name):
#     return f'Hello, {name}!'


# result = greet('David')

# print(result)




'   The generic decorator structure'

# def outer_function(argument_function):

#     def inner_function(*args):

#         print('The inner function is doing something...')

#         return(argument_function(*args))
    
#     return inner_function


# @outer_function
# def argument_function(argument):
#     return f'The argugment function is doing something with the {argument}!'


# result = argument_function('*Argument*')

# print(result)




'   A practical application'

# def timer_func(func):

#     def wrapper(*args):

#         s = timer()
#         func()
#         e = timer()-s

#         print(f"It took {e:.2f}s to execute '{func.__name__}()' function")
        
    
#     return wrapper


# @timer_func
# def do_this():
#     time.sleep(2.54)
    

# do_this()




'   Stacked decorators application'

# def uppercase_decorator(func):

#     def wrapper(*args):
        
#         result = func(*args)

#         return result.upper()
            
#     return wrapper


# def greeting_decorator(func):

#     def wrapper(*args):
        
#         result = func(*args)

#         return f"Greeting, {result}"
            
#     return wrapper


# @uppercase_decorator
# @greeting_decorator
# def greet(name):
#     return f"Hello, {name}!"


# result = greet('David')

# print(result)




'   A more sophisticated example'

# def repeat(n_times):

#     def decorator(func):

#         def wrapper(*args, **kwargs):

#             for _ in range(n_times):

#               func(*args, **kwargs)             
                             
#         return wrapper
    
#     return decorator



# @repeat(n_times=3)
# def greet(name):
#     return print(f"Hello, {name}!")


# greet("Alice")






"Patrick Loeber Tutorial"

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):

#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')

#         return result
    
#     return wrapper


# @start_end_decorator
# def add5(x):
#     return x + 5


# # result = add5(10)
# # print(result)

# print(help(add5))
# print(add5.__name__)    # add5




'   Class decorators'

# class CountCalls:

#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0

#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f'This have been executed {self.num_calls} times')
#         return self.func(*args, **kwargs)


# @CountCalls
# def say_hello():
#     print('Hello!')


# say_hello()
# say_hello()






"Corey Scheafer Tutorial"


# def my_logger(orig_func):

#     import logging
#     logging.basicConfig(filename = f'{orig_func.__name__}.log', level=logging.INFO)

#     @functools.wraps(orig_func)
#     def wrapper(*args, **kwargs):

#         logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):

#     import time

#     @functools.wraps(orig_func)
#     def wrapper(*args, **kwargs):

#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1

#         print(f'{orig_func.__name__} ran in: {t2:.2f} sec')

#         return result

#     return wrapper


# @my_logger
# @my_timer
# def display_info(name, age):

#     time.sleep(1)
#     print(f'display_info ran with arguments ({name}, {age})')



# display_info('Tom', 22)

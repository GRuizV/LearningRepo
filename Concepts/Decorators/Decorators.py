from timeit import default_timer as timer
import time 


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



















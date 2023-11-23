from timeit import default_timer as timer

' Do private attribute can be accessed by derived classes?'

# ' With name-tricking it'
# class A:

#     __priv_a_cls_att = 'Private A class Attribute'

#     def __init__(self):

#         self.__priv_a_ins_att = 'Private A class Instance Attribute'
#         pass

# class B(A):
#     pass


# print(f"Accessing from an instance of A: {A()._A__priv_a_ins_att}") # Accessing from an instance of A: Private A class Instance Attribute
# print(f"Accessing from the A Class: {A._A__priv_a_cls_att}", end="\n\n")    # Accessing from the A Class: Private A class Attribute


# print(f"Accessing from an instance of B: {B()._A__priv_a_ins_att}") # Accessing from an instance of B: Private A class Instance Attribute
# print(f"Accessing from the B Class: {B._A__priv_a_cls_att}")    # Accessing from the B Class: Private A class Attribute


# 'With ChatGPTs Example'

# class Parent:
#     def __init__(self):
#         self.__private_attr = 10

#     def get_private_attr(self):
#         return self.__private_attr


# class Child(Parent):
#     def __init__(self):
#         super().__init__()

#     def access_private_attr(self):
#         # This won't work directly:
#         # print(self.__private_attr)

#         # But this will, using the method from the parent class:
#         print(self.get_private_attr())


# child = Child()
# child.access_private_attr()  # This will print 10







" What's the correct order or arguments in functions?"

# # This one
# def example_function(pos_arg1, pos_arg2, default_arg1="default", *args, kwarg1, kwarg2="value", **kwargs):

#     # pos_arg1 and pos_arg2 are positional arguments
#     # default_arg1 is a default argument
#     # *args collects extra positional arguments
#     # kwarg1 and kwarg2 are keyword arguments with kwarg2 having a default value
#     # **kwargs collects extra keyword arguments
    
#     print("Positional arguments:", pos_arg1, pos_arg2)
#     print(f"Default argument: {default_arg1} / which is still needed to be passed")
#     print("Arbitrary positional arguments (*args):", args) # if default_arg1 is not passed, any arb pos arg would be assumed as default arg1
#     print(f"Keyword arguments:'{kwarg1}', '{kwarg2}'")  # funny that the kw default "value" does not need to be passed, opposite to the default positional argument.
#     print("Arbitrary keyword arguments (**kwargs):", kwargs)

# # Example function call
# example_function(1, 2, "default", 'arb_arg1', 'arb_arg2', 'arb_arg3', kwarg1="keyword_arg", extra_arb_kwarg1="kw value 1", extra_arb_kwarg2="kw value 2")






" What does the filter() function do?"

'''
    The filter() function in Python is used to filter elements from an iterable (like a list) 
    based on a specified function. It returns an iterator that contains the elements for which the function returns True.
    
    the syntax of the function is:filter(function, iterable)
'''

# #input
# numbers = [x for x in range(10000)]



# # Function to check if a number is even
# def is_even(num):
#     return num % 2 == 0

# # Use filter() to get only even numbers
# s = timer()
# even_numbers = list(filter(is_even, numbers))
# e = timer()

# # print(even_numbers)  # Output: [2, 4, 6, 8, 10]
# print(f"with classic func statement, time: {e-s:.2E}s")


# "   Let's try with a lambda to do the same"

# s = timer()
# even_numbers = list(filter(lambda x: True if x%2 == 0 else False, numbers ))
# e = timer()

# # print(even_numbers)  # Output: [2, 4, 6, 8, 10]
# print(f"with lambda func def, time: {e-s:.2E}s")



# "   now, would it be faster with a listcomp?"

# s = timer()
# even_numbers = [x for x in numbers if x%2 == 0]
# e = timer()

# # print(even_numbers)  # Output: [2, 4, 6, 8, 10]
# print(f"with Listcomp, time: {e-s:.2E}s")


# '''
#     After some runs, the top in performance tends to be:
#         1. Listcomp
#         2. Classic Func Def
#         3. With a lambda Def

#     And according to ChatGPT:
#     Given the size of the range (10,000 elements), here's an estimation of how the methods might perform:

#         1. List comprehension: This method tends to be very efficient for such straightforward operations in Python. It often performs well due to its optimized nature.

#         2. Filter with a lambda function: While filter() with a lambda function is concise, it might be slightly slower than a list comprehension due to the overhead of creating a lambda function for each element.

#         3. Filter with a separate function: Creating a separate function adds some overhead, similar to using a lambda function, but it could potentially be slightly slower due to the function call.
# '''
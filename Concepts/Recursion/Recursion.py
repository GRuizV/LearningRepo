import sys
from timeit import timeit
import statistics


"First Basic Recursion Case: Fibonacci's sequence"

# # Base case
# def factorial (n):

#     if n == 0: return 1
#     return n * factorial(n-1)


# # Case with print statements
# def factorial (n):

#     if n == 0:
#         print(f'f(0) = 1')
#         return 1
    
#     else:
#         result = n * factorial(n-1)
#         print(f'f({n}) = {n} * f({n-1}) = {result}')
#         return result


# n = 5

# # for base case
# a = factorial(n)
# print(a)    # Result = 120

# # for pint case
# print(f'factorial of "{n}" is:', end='\n\n')
# factorial(n)





"Second Basic Recursion Case: Fibonacci's sequence"

# # Basic fibonacci's form
# def fibonacci(n):

#     if n == 0: return 0
#     if n == 1: return 1
    
#     return fibonacci(n-2) + fibonacci(n-1)

# n = 6
# result = fibonacci(n)

# print(result)   # Result: 8




# # Fibonacci's but printouts
# def fibonacci(n):

#     ''' 
#     This was my attempt to get a clean printout of the fibonacci's seq numbers
#     but turned out to be an unexpected but valuable result, since it showed me
#     how recursion actually flows: Goes from bottom-up from left to right, if a tree-like
#     representation were drawn to understand the recursion
#     '''

#     if  n == 0:
#         print('F(0) = 0')          
#         return 0       

#     if n == 1:
#         print('F(1) = 1') 
#         return 1   
    
#     else:        
#         result = fibonacci(n-1) + fibonacci(n-2)
#         print(f'F({n}) = F({n-1}) + F({n-2}) = {result}')
#         return result
    

# n = 5
# fibonacci(n)




'Now, with the correct printouts'

# # Base algorithm
# def fibonacci(n):

#     if n == 0: return 0
#     if n == 1: return 1
    
#     return fibonacci(n-1) + fibonacci(n-2)


# def fib_printouts(n):
    
#     for i in range(n+1):

#         if i == 0:
#             print(f'F({i}) = {fibonacci(i)}')

#         elif i == 1:          
#             print(f'F({i}) = {fibonacci(i)}')

#         else:
#             print(f'F({i}) = {fibonacci(i)}')

# # n = 5
# # fib_printouts(n)



# # I think it'd be better to return just a list of Fib's seq. up to the result 
# def fib_seq(n):
    
#     result = [0,1]

#     # # This is fine but could be more elegant
#     # for i in range(2, n+1):
#     #     result.append(fibonacci(i))

#     # return result

#     # This is more elegant!
#     [result.append(fibonacci(i)) for i in range(2, n+1)]
#     return result


# n = 5
# fib_seq_utn = fib_seq(n)

# print(f"Fibonacci's sequence up to '{n}':")
# print(fib_seq_utn)




# "This is my definitive version of the Fibonacci's Seq generator based on recursion"

# def fib_seq(n):

#     def fibonacci(n):

#         if n == 0: return 0
#         if n == 1: return 1
        
#         return fibonacci(n-1) + fibonacci(n-2)
    
#     result = [0,1]

#     [result.append(fibonacci(i)) for i in range(2, n+1)]
#     return result


# print(fib_seq(5))





"Another simple case: sum up to something"

# # Base case
# def rec_sum(n):

#     if n == 1:       
#         return 1
   
#     return n + rec_sum(n-1)


# n = 5
# print(rec_sum(n))




# # Case with printouts
# def rec_sum(n):

#     if n == 1:
#         print(f'It starts with: 1')
#         return 1
    
#     result = n + rec_sum(n-1)  
#     print(f'{result-n} + {n} = {result}')
#     return result


# n = 5
# rec_sum(n)





"Other notes on recursion"


'This is the recursion limit for this machine'
# # By deafult, python sets it to 1000
# print(sys.getrecursionlimit())




'''
The factorial function again, but better established to show
how the recursion makes the calls
'''

# def factorial(n):

#     print(f"factorial() called with n = ({n})")

#     return_val = 1 if n == 0 else n * factorial(n-1)

#     print(f"-> factorial({n}) returns {return_val}")

#     return return_val


# factorial(5)

# # The printouts are clearer this way

# '''
#     factorial() called with n = (5)
#     factorial() called with n = (4)
#     factorial() called with n = (3)
#     factorial() called with n = (2)
#     factorial() called with n = (1)
#     factorial() called with n = (0)
#     -> factorial(0) returns 1
#     -> factorial(1) returns 1
#     -> factorial(2) returns 2
#     -> factorial(3) returns 6
#     -> factorial(4) returns 24
#     -> factorial(5) returns 120
# '''




'''
Now, we will compare execution times with recursion 
'''


# # First, this will be the metric to measure

# code_to_measure = 'print(string)'
# setup_code = "string = 'foobar'"

# exec_time = timeit(code_to_measure, setup_code, number=100)

# # Executed in 0.010
# print(f'Executed in {exec_time:.3f}s')



# # Now, with the actual example

# # The recursive case
# setup_string = """
# def factorial(n):
#     return 1 if n <= 1 else n * factorial(n - 1)
# """
# exec_time = timeit('factorial(4)', setup_string, number=1000000)

# # The code took 3.627s to complete
# print(f"Recursive: {exec_time:.3f}s")



# # The non-recursive case
# setup_string = """
# def factorial(n):
#     return_value = 1
#     for i in range(2, n+1):
#         return_value *= 1
#     return return_value
# """
# exec_time = timeit('factorial(4)', setup_string, number=1000000)

# # The code took 1.393s to complete
# print(f"Iterative: {exec_time:.3f}s")




'''
Recursion for Nested List Traversals 
'''

# Let's consider this list
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]


# Now, is requiered to know how many name are contained in the list


'   My attempt to do it so recursively'
# def item_counter(item_list):

#     print(f"List: {item_list}")
#     count = 0

#     for item in item_list:

#         if isinstance(item, list):
#             print('Encountered Sublist')
#             count += item_counter(item)
        
#         else:
#             print(f"Counted leaf item '{item}'")
#             count += 1

#     print(f"-> Returning count: {count}")
#     return count
# # works fine

# item_counter(names) # The answer is 10



"   Non-recursive version"
# def item_counter(item_list):

#     count = 0
#     stack = list()
#     element = item_list
#     i = 0

#     while True:

#         if i == len(element):

#             if element == item_list:
#                 return count
            
#             else:
#                 element, i = stack.pop()
#                 i += 1
#                 continue
            

#         if isinstance(element[i], list):

#             stack.append([element, i])
#             element = element[i]
#             i = 0
            
#         else:
#             count += 1
#             i += 1


# print(item_counter(names))




'''
Detecting Palindromes 
'''


'   My attempt to make a function that detects palindromes recursively'

# Criteria for being a Palindrome (Actually, taken from RealPython)
#   1. If len(substring) == 1 is a palindrome.
#   2. First and last character are equal.


# def is_palindrome(string):

#     if len(string) <= 1:
#         return True

#     if string[0] == string[-1]:
#         return is_palindrome(string[1:-1])
    
#     else:
#         return False
    

# print(is_palindrome(''))




'''
Sort with QuickSort
'''


def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers
    
    else:

        pivot = statistics.median([numbers[0], numbers[len(numbers)//2], numbers[-1]])

    items_less = [num for num in numbers if num < pivot]
    pivot_items = [num for num in numbers if num == pivot]
    items_greater =  [num for num in numbers if num > pivot]


    return quick_sort(items_less) + pivot_items + quick_sort(items_greater)




testing_numbers = [24, 4, 67, 71, 84]



result = quick_sort(testing_numbers)

print(result)
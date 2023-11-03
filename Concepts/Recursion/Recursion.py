
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
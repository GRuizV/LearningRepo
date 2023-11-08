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

# def quick_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers
    
#     else:

#         pivot = statistics.median([numbers[0], numbers[len(numbers)//2], numbers[-1]])

#     items_less = [num for num in numbers if num < pivot]
#     pivot_items = [num for num in numbers if num == pivot]
#     items_greater =  [num for num in numbers if num > pivot]


#     return quick_sort(items_less) + pivot_items + quick_sort(items_greater)




# testing_numbers = [24, 4, 67, 71, 84]



# result = quick_sort(testing_numbers)

# print(result)




'''
Thinking Recursively - Santa's Presents Deliveries
    RealPython Article
'''


# houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# # Iterative Solution
# def ite_deliver_presents():

#     for house in houses:
#         print("Delivering presents to", house)
 

# ite_deliver_presents()




# # Recursive Solution

# def rec_deliver_presents(houses):

#     # Worker Elf doing his job
#     if len(houses) == 1:
#         house = houses[0]
#         print("Delivering presents to", house)


#     # Manager Elf doing his job
#     else:
#         mid = len(houses) // 2
#         sub_houses_1 = houses[:mid]
#         sub_houses_2 = houses[mid:]

#         # Dividing the work between two elves
#         rec_deliver_presents(sub_houses_1)
#         rec_deliver_presents(sub_houses_2)


# rec_deliver_presents(houses)




'''
Recursion Cases interpretation
    Geeks for geeks Article
'''

'case 1'
# def fun1(x, y) : 
  
#     if (x == 0) : 
#         return y 
    
#     else : 
#         return fun1(x - 1, x + y) 

# # if x=3, y=5, results are: 8, 10, 11 
# print(fun1(3,5))

'''
My interpretation:
    Is the sum of the numbers from 0 to x to a constant 'y'

According to Geeks for geeks:
    is the expansion of the ecuation:    x(x+1)/2 + y
'''




'Try to predict the output of this'

# def fun(x):
     
#     if(x > 0):
#         x -= 1
#         fun(x) 
#         print(x , end=" ")
#         x -= 1
#         fun(x) 
         
# # Driver code
# a = 4
# fun(a)  # Printout: 0 1 2 0 3 0 1 

'''
This is the recursion tree:

                   fun(4);
                   /
                fun(3), print(3), fun(2)(prints 0 1)
               /
           fun(2), print(2), fun(1)(prints 0)
           /
       fun(1), print(1), fun(0)(does nothing)
       /
    fun(0), print(0), fun(-1) (does nothing)

'''




'Try to predict the output of this'

# def fun(a, n):

#     if(n == 1): 
#         return a[0]
    
#     else:
#         x = fun(a, n - 1)

#     if(x > a[n - 1]):
#         return x
    
#     else:
#         return a[n - 1]
 
# # Driver code
# arr = [12, 10, 30, 50, 100]
# print(fun(arr, 5))

'The answer: 100'




'Try to predict the output of this'

# def fun(i): 
 
#     if (i % 2 == 1):
#         i += 1
#         return (i - 1)
    
#     else:
#         return fun(fun(i - 1))
   
# print(fun(200))

'The answer: 199'




'Try to predict the output of this'

# def fun(a, b):

#     if (b == 0):
#         return 0
    
#     if (b % 2 == 0):
#         return fun(a + a, b//2) 
     
#     return fun(a + a, b//2) + a 
 
# # Driver code 
# print(fun(4, 4))

'The answer: 12'




'Try to predict the output of this'

# def fun(a, b):
#     if (b == 0):
#         return 1
#     if (b % 2 == 0):
#         return fun(a*a, b//2) 
     
#     return fun(a*a, b//2)*a 
  
# # Driver code
  
# print(fun(4, 3))

'The answer: 64'
 



'Try to predict the output of this'

# def fun(n):
     
#     if (n > 100):
#         return n - 10
     
#     return fun(fun(n + 11))
     
# # Driver code
# print(fun(99))

'The answer: 91'
 



'Give the relation between len() and the characters printed'

# def abc(s):
#     if(len(s) == 0):
#         return
     
#     abc(s[1:])
#     abc(s[1:])
#     print(s[0])

# s = 'abc'

# abc(s)

'''
The answers:

num = 2^len-1

s[0] is 1 time printed
s[1] is 2 times printed
s[2] is 4 times printed

s[i] is printed 2^i times

s[strlen(s)-1] is printed 2^(strlen(s)-1) times

total = 1 + 2 +....+ 2^(strlen(s)-1) = (2^strlen(s)) - 1

'''




'Try to predict the output'

# def fun(count):

#     print(count)

#     if(count < 3):

#         count+=1
#         fun(fun(fun(count))) 
     
#     return count 


# fun(1)

'''
The answers: 1 2 3 3 3 3 3
'''




'Try to predict the output'

# fp = 15
  
# def fun(n): 

#     global fp 

#     if (n <= 2): 
#         fp = 1
#         return 1
  
#     t = fun(n - 1) 
#     f = t + fp 
#     fp = t 

#     return f 
  
# # Driver code 
# print(fun(5))


'''
The answers: 5
'''




"Tower of Hanoi Puzzle"


'Recursive solution'
c = 1

def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    global c
    if n == 0:
        return

    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(c, "Move disk", n, "from rod", from_rod, "to rod", to_rod)
    c+=1
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

n = 3

# tower_of_hanoi(n, "A", "C", "B")




'Iterative Solution'

# Python3 program for iterative Tower of Hanoi
import sys
 
# A structure to represent a stack
class Stack:
    # Constructor to set the data of
    # the newly created tree node
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0]*capacity
 
# function to create a stack of given capacity.
def createStack(capacity):
    stack = Stack(capacity)
    return stack
  
# Stack is full when top is equal to the last index
def isFull(stack):
    return (stack.top == (stack.capacity - 1))
   
# Stack is empty when top is equal to -1
def isEmpty(stack):
    return (stack.top == -1)
   
# Function to add an item to stack.
# It increases top by 1
def push(stack, item):
    if(isFull(stack)):
        return
    stack.top+=1
    stack.array[stack.top] = item
   
# Function to remove an item from stack.
# It decreases top by 1
def Pop(stack):
    if(isEmpty(stack)):
        return -sys.maxsize
    Top = stack.top
    stack.top-=1
    return stack.array[Top]
   
# Function to implement legal
# movement between two poles
def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = Pop(src)
    pole2TopDisk = Pop(dest)
 
    # When pole 1 is empty
    if (pole1TopDisk == -sys.maxsize):
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
       
    # When pole2 pole is empty
    elif (pole2TopDisk == -sys.maxsize):
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
       
    # When top disk of pole1 > top disk of pole2
    elif (pole1TopDisk > pole2TopDisk):
        push(src, pole1TopDisk)
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
       
    # When top disk of pole1 < top disk of pole2
    else:
        push(dest, pole2TopDisk)
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
   
# Function to show the movement of disks
def moveDisk(fromPeg, toPeg, disk):
    print("Move the disk", disk, "from '", fromPeg, "' to '", toPeg, "'")
   
# Function to implement TOH puzzle
def tohIterative(num_of_disks, src, aux, dest):
    s, d, a = 'S', 'D', 'A'
   
    # If number of disks is even, then interchange
    # destination pole and auxiliary pole
    if (num_of_disks % 2 == 0):
        temp = d
        d = a
        a = temp
    total_num_of_moves = int(pow(2, num_of_disks) - 1)
   
    # Larger disks will be pushed first
    for i in range(num_of_disks, 0, -1):
        push(src, i)
   
    for i in range(1, total_num_of_moves + 1):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(src, dest, s, d)
   
        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(src, aux, s, a)
   
        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(aux, dest, a, d)
 
# Input: number of disks
num_of_disks = 3
 
# Create three stacks of size 'num_of_disks'
# to hold the disks
src = createStack(num_of_disks)
dest = createStack(num_of_disks)
aux = createStack(num_of_disks)
 
tohIterative(num_of_disks, src, aux, dest)






from timeit import default_timer as timer


'''
    6. Write a Python program to convert a tuple to a string.
   
'''

# tuple1 = (1, 2, 3, 4)

# s = str()

# # My Approach

# for elem in list(map(str,tuple1)):

#     s += elem

# print(s)

''' ----------- '''

# # Page's approach

# s = ''.join(map(str, tuple1))

# print(s)



'''
    16. Write a Python program to convert a tuple to a dictionary.
   
'''


# tuplex = ((2, "w"),(3, "r"))

# d = { k:v for (k, v) in tuplex }

# print(d)



'''
    17. Write a Python program to unzip a list of tuples into individual lists.
   
'''

# l = [(1,2), (3,4), (8,9)]

# # My approach

# l1 = [ x[0] for x in l ]

# l2 = [ x[1] for x in l ]

# print(f'{l1}\n{l2}')

''' ----------- '''

# # Page's approach

# l = list(zip(*l)) #This takes the idea that unzipping something is just matter to apply the zip() function again, and actually makes sense

# l1, l2 = l

# print(f'{l1}\n{l2}')



'''
    21. Write a Python program to replace the last value of tuples in a list.

    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
   
'''


# l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# l = [ elem[:-1] + (100,) for elem in l ]

# print(l)




'''
    22. Write a Python program to remove an empty tuple(s) from a list of tuples.

    Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
   
'''

# # My approach

# input = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# result = [ elem for elem in input if len(elem) != 0 ]

# print(result)


# # Page's approach

# input = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# result = [ elem for elem in input if elem ] #The difference is that it takes that every elem is True if is not empty

# print(result)




'''
   23. Write a Python program to sort a tuple by its float element. 
   
    Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
   
'''

# input = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# result = [ elem for elem in sorted(input, key = lambda x: x[1], reverse = True) ]

# print(result)




'''
   24. Write a Python program to count the elements in a list until an element is a tuple. 
   
  
'''


# nums = [0, 10, 20, 30, (10,20), 40]


# # My initial approach

# count = 0

# for elem in nums:

#     if type(elem) == tuple: break

#     count += 1

# print(count)


''' ------------ '''


# # My later oneliner approach

# count = len( nums[ : list( map( type, nums) ).index( tuple ) ] )

# print(count)


''' ------------ '''


# # Page's approach

# ctr = 0

# for n in nums:

#     if isinstance(n, tuple):

#         break

#     ctr += 1

# print(ctr)



'''
   25. Write a Python program to convert a given string list to a tuple.

    Original string: 'python 3.0'
    
    Convert the said string to a tuple:
    ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0') 
   
'''

# input_string = 'python 3.0'

''' ------------ '''

# # My approach

# result = tuple( char for char in input_string)

# print(result)




'''

  26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.

    Original Tuple:
    (4, 3, 2, 2, -1, 18)
    Product - multiplying all the numbers of the said tuple: -864

    Original Tuple:
    (2, 4, 8, 8, 3, 2, 9)
    Product - multiplying all the numbers of the said tuple: 27648   
  
'''

# import math

# t = (4, 3, 2, 2, -1, 18)

''' ------------ '''

# # My original approach

# result = 1

# for elem in t:  result *= elem

# print(result)

''' ------------ '''

# # math prod() function approach

# print(math.prod(t)) # prod() does the same as sum() but with multiplication



'''

  27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.

    Original Tuple:
    ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

    Average value of the numbers of the said tuple of tuples:
    [30.5, 34.25, 27.0, 23.25]

    Original Tuple:
    ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

    Average value of the numbers of the said tuple of tuples:
    [25.5, -18.0, 3.75]
    
  
'''


# tuples_tuple = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))


''' ------------ '''

# # Looping approach

# result = list()

# for i in range(len(tuples_tuple[0])):

#     avg = 0

#     for j in range(len(tuples_tuple)):

#         avg += tuples_tuple[j][i]
    
#     result.append( avg / len(tuples_tuple) )

# print(result)
    


''' ------------ '''


# # Page's approach

# result = [ sum(tupl) / len(tupl) for tupl in zip(*tuples_tuple) ] # I really like this tho

# print(result)




'''
28. Write a Python program to convert a tuple of string values to a tuple of integer values.

    Original tuple values:
    (('333', '33'), ('1416', '55'))

    New tuple values:
    ((333, 33), (1416, 55))

'''


tupl = (('333', '33'), ('1416', '55'))

''' ------------ '''

# # tupcomp approach

# result = tuple( (int(elem[0]), int(elem[1])) for elem in tupl  )

# print(result)

''' ------------ '''

# # map() approacch

# result = tuple ( tuple( map( int, elem ) ) for elem in tupl ) # At the end a comprehension had to be done, so stalemate 

# print(result)



'''
29. Write a Python program to convert a given tuple of positive integers into an integer.

    Original tuple:
    (1, 2, 3)

    Convert the said tuple of positive integers into an integer:
    123

    Original tuple:
    (10, 20, 40, 5, 70)

    Convert the said tuple of positive integers into an integer:
    102040570

'''

# tupl = (10, 20, 40, 5, 70)

# # My approach

# result = str()

# for elem in tupl: result += str(elem)

# print(result)


''' ------------ '''

# # Page's Approach

# result = ''.join(map(str,tupl))

# print(result)




''' 
    30. Write a Python program to check if a specified element appears in a tuple of tuples.
    
    Original list:
    (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
    
    Check if White presenet in said tuple of tuples!
    True
    
    Check if Purple presenet in said tuple of tuples!
    True
    
    Check if Olive presenet in said tuple of tuples!
    False
'''


# tupl = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

# comp = 'Purple'

# result = any([ any([ elem == comp for elem in tup ]) for tup in tupl])

# print(f'Check if "{comp}" presenet in said tuple of tuples!')

# print(result)



''' 
   31. Write a Python program to compute the element-wise sum of given tuples. 

    Original lists:
    (1, 2, 3, 4)
    (3, 5, 2, 1)
    (2, 2, 3, 1)

    Element-wise sum of the said tuples:
    (6, 9, 8, 6)

'''

# tupl1 = (1, 2, 3, 4)
# tupl2 = (3, 5, 2, 1)
# tupl3 = (2, 2, 3, 1)

''' ------------ '''

# # My approach

# result = tuple( sum(elem) for elem in zip(tupl1, tupl2, tupl3))

# print(result)

''' ------------ '''

# # Page's approach

# result = tuple( map(sum, zip(tupl1, tupl2, tupl3)) ) # More efficient

# print(result)



''' 
    32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
    
    Original list of tuples:
    [(1, 2), (2, 3), (3, 4)]
    
    Sum of all the elements of each tuple stored inside the said list of tuples:
    [3, 5, 7]
    
    Original list of tuples:
    [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
    
    Sum of all the elements of each tuple stored inside the said list of tuples:
    [9, -1, 7, 8]

'''


# tupl = [(1, 2), (2, 3), (3, 4)]

# # My approach

# result = list( map(sum, tupl) ) # The two lines does de same but this one is more efficient

# result = [ sum(elem) for elem in tupl ]

# print(result)



''' 
    33. Write a Python program to convert a given list of tuples to a list of lists.
    
    Original list of tuples: [(1, 2), (2, 3), (3, 4)]
    Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]

    Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
    Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

'''


# tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

# result = list( map( list, tuples ) ) #The most efficient way would be this one

# print(result)
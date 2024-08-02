from timeit import default_timer as timer


''' Here is how we pass from a nested loop to a nested list comprehension'''


'''First a simple for-in & simple list comprehension:'''

# # Let's state a parameter (x) to build lists from there

# x = 5 


# #forin:

# list_forin_x = []

# for i in range(x):
#     list_forin_x.append(i)

# print(list_forin_x)


# '''
# The output  in both cases must be:

# [0, 1, 2, 3, 4]

# '''


# #list comprehension:

# list_compr_x = [i for i in range(x)]

# print(list_compr_x)


# # Here, this two ways a fairly simple and similar




'''Now let's do the same but with a 2D array (a list of list cointaining two-elements):'''

# #Let's state a parameter (x) and (y) to build lists from there

# x = 5 
# y = 5 



# # forin:

# list_forin_xy = []

# for i in range(x):
   
#     for j in range(y):

#         list_forin_xy.append([i,j])
    
    
# print(list_forin_xy)


# '''
# The output  in both cases must be:

# [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]

# '''


# # list comprehension:

# list_compr_xy = [ [i,j] for i in range(x) for j in range(y)]

# print(list_compr_xy)






'''Finally we are going to build a 3D array (a list of lists containing three elements):'''


# #Let's state a parameter (x), (y) and (z) to build lists from there

# x = 5
# y = 5
# z = 5


# #forin:


# list_forin_xyz = []

# start = timer()

# for i in range(x):
    
#     for j in range(y):

#         for k in range(z):

#             list_forin_xyz.append([i,j,k])

# stop = timer()

# print(f'\n{stop-start}\n')

# # print(list_forin_xyz)


# '''
# The output should be for both cases:

# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 
# 2], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

# '''

# #list comprehension:


# # start = timer()

# list_compr_xyz = [ [i,j,k] for i in range(x) for j in range(y) for k in range(z)]

# # stop = timer()

# # print(f'\n{stop-start}\n')

# # print(list_compr_xyz)



'''
List comprehension Final comments:

The two operations apparently are similar but in terms of resources cosumption, the discussion on StackOverflow is that
list comprehesions are more demanding and waste more memory than a nested for loop.

    My experiments calculation the time taken on each operation points out that on smaller operations (x=5, y=5, z=5) for loops go faster, 
    but in big operations (x=100, y=100, z=100) the list comprehension performs pretty similar and sligthly better than for loops.

'''











''' 

Just as a test

--- I will try to build a 2D array with list comprehension structure ---

'''

# #Let's state a parameter (x) and (y) to build lists from there

# x = 5 
# y = 5 



# # forin:

# list_forin_xy = []

# for i in range(x):
#    temp = []

#    for j in range(y):
#     temp.append([i,j])

#    list_forin_xy.append(temp)
    

# for i in list_forin_xy:

#     print(i)


# '''
# The output  in both cases must be:

# [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
# [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]
# [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4]]
# [[3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
# [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]

# '''


# # list comprehension:

# list_compr_xy = [ [[i,j] for j in range(y)] for i in range(x)]

# for i in list_compr_xy:
#     print(i)


# #SUCCEED









''' 

And, now... 

--- I will try to build a 3D array with list comprehension structure ---

'''

# #Let's state a parameter (x), (y) and (z) to build lists from there

# x = 5
# y = 5
# z = 5



# # forin:

# list_forin_xyz = []

# start = timer()

# for i in range(x):
#     temp=[]

#     for j in range(y):

#         for k in range (z):
#             temp.append([i,j,k])
        
#     list_forin_xyz.append(temp)
    
# stop = timer()

# print(stop-start)

# # for i in list_forin_xyz:
# #     print(i)


# '''
# The output  in both cases must be:

# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2]]
# [[1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2]]
# [[2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

# '''


# # list comprehension:

# list_compr_xyz = [ [[i,j,k] for j in range(y) for k in range(z)] for i in range(x)]

# stop = timer()

# print(f'\n{stop-start}')

# # for i in list_compr_xyz:
# #     print(i)


# #SUCCEED



'''
Arrays creation Final comments: Different from List Comprehension, when it comes to create an Array, for in loop always go faster non-regarding the size of the operations

'''


''' ----------- '''



'''
Flatening a list of lists with listcomp and two 'for's
'''

# vec = [[1,2,3], [4,5,6], [7,8,9]]

# new_list = [num for elem in vec for num in elem]

# print(new_list)

# #Example of a listcomp with two fors whith one condition
# listcomp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# print(listcomp)




'''
Transposing a matrix
'''

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# transposed = [[row[i] for row in matrix] for i in range(4)]

# print(transposed)


# # which will be the same as

# transposed = []

# for i in range(4):

#     transposed_row = []
    
#     for row in matrix:

#         transposed_row.append(row[i])
    
#     transposed.append(transposed_row)

# print(transposed)

# # The Python documentation recommends to use Built-in function to cases like to to avoid unnecessary complexity

# transposed = list(zip(*matrix))

# print(transposed)





''' More ListComp exercices '''


# # I want (letter, num) pair for each letter in 'abcd' and each number in '0123'.

# pairs = list()

# for letter in 'abcd':

#     for num in '0123':

#         pairs.append((letter, num))


# pairs = [ (letter, num) for num in '0123' for letter in 'abcd']

# print(pairs)


'''----------------'''

# # Dictionary Comprehensions

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# dict1 = dict()

# for i in range(len(names)):

#     dict1[names[i]] = heros[i]


# dict1 = { names[i]: heros[i] for i in range(len(names))  } # This is one way to do it

# dict1 = { name : hero for name, hero in zip(names, heros)  } # This is another way to do it

# print(dict1)


'''----------------'''


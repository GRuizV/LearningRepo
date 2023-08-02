'''
Problem: Given a square matrix [n] x [n], rearrange in asceding orders the numbers to return it

input:
[3, 2]
[8, 4]

output:
[2, 3]
[4, 8]


input:
[3, 2, 5]
[8, 4, 3]
[7, 4, 1]

output:
[1, 2, 3]
[3, 4, 4]
[5, 7, 8]


'''

# # Came out with this solution based on ListsComp on 9/2/23

# in_matrix = [[3,2], [8,4]]

# print(f'Original array: {in_matrix}')

# list1 = [ x for y in in_matrix for x in y  ]

# list1.sort()

# # This is how flatten lists are deployed after sorting.
# # list1 = [2, 3, 4, 8]
# # list1 = [1, 2, 3, 3, 4, 4, 5, 7, 8]  
# # list1 = [1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8, 9, 9, 9]

# if len(in_matrix) == 2:
    
#     out_matrix = [ [list1[ 2 * i ], list1[ 2 * i + 1 ] ] for i in range(len(in_matrix)) ] # Solution for a [2]x[2] problem

# elif len(in_matrix) == 3:

#     out_matrix = [ [list1[ 3 * i ], list1[ 3 * i + 1 ], list1[ 3 * i + 2 ] ] for i in range(len(in_matrix)) ] # Solution for a [3]x[3] problem

# elif len(in_matrix) == 4:

#     out_matrix = [ [list1[ 4 * i ], list1[ 4 * i + 1 ], list1[ 4 * i + 2 ], list1[ 4 * i + 3 ]  ] for i in range(len(in_matrix)) ] # Solution for a [4]x[4] problem


# print(f'Arranged array: {out_matrix}')

# # The problem with this approach is that is non-escalable compared to the forloop's approach. I just did it as exercise for ListComps.




''' -------------- '''




'''This is how to create a matrix'''

# array_dimention = int(input('To build de array give me a size:'))

# list_out = []

# print('\nlets populate the array')

# for i in range(array_dimention):
#     print(f'this is the row # {i}')

#     list_in = []                    #Is important that this list is created WITHIN the first for loop, otherwise it won't populate correctly the matrix
    
#     for n in range(array_dimention):
#         print(f'this is the element #{n} of the row #{i}')
#         list_in.append(int(input('')))
    
#     list_out.append(list_in)

    
'''Having it created, let's make a sorting algorythm'''


# [[3,2], [8,4]]  
# [[3,2,5], [8,4,3], [7,4,1]]
# [[7,9,3,1], [5,6,7,9], [9,6,7,2], [4,1,6,8]]


# matrix = [[7,9,3,1], [5,6,7,9], [9,6,7,2], [4,1,6,8]]        #This will be the sample matrix

# new_matrix = []

# for i in matrix:
#     for j in i:
#         new_matrix.append(j)


# new_matrix = sorted(new_matrix, key=None, reverse=False)

# final_matrix = []


# count = 0

# for i in range(len(matrix)):
#     temp_list=[]

#     for j in range(len(matrix[i])):
#         temp_list.append(new_matrix[count])
#         count += 1
           
#     final_matrix.append(temp_list)
    


# for i in matrix: print(i)

# print('\n')

# for i in final_matrix: print(i) 



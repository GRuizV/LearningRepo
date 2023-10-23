import math
import itertools
import collections
import random



"Ema's Supercomputer"

# # Input
# a = '''BGBBGB
# GGGGGG
# BGBBGB
# GGGGGG
# BGBBGB
# BGBBGB'''

# grid = [x for x in a.split('\n')]


grid = ['BGBBBBB','GGGBBBB','BGBBGBB','BBBBGBB','BBGGGGG','BBBBGBB','BBBBGBB']

for i in grid: print(i)
print()




# My solution

'Auxiliary Function'
# # a plus argument comes in the form "[Plus' area, (i, j)]"    being i,j the coordinates
# def plus_checker(plus):

#     if plus:

#         try:
#             area = plus[0]
#             up = plus[1][0]
#             down = plus[1][1]
#             left = plus[1][2]
#             right = plus[1][3]

#             if 'B' not in ( grid[up[0]-1][up[1]], grid[down[0]+1][down[1]], grid[left[0]][left[1]-1], grid[right[0]][right[1]+1] ):

#                 return [ area + 1, ( (up[0]-1, up[1]), (down[0]+1, down[1]), (left[0], left[1]-1), (right[0],right[1]+1) ) ]

#         except IndexError:

#             return        

    

'Body of the main function'
# possible_p = list()

# for row in range(1, len(grid[1:-1])+1):
    
#     for j in range(1, len(grid[row][1:-1])+1):

#         if 'B' not in (grid[row-1][j], grid[row+1][j], grid[row][j-1], grid[row][j+1]):

#             # Stored as "[Plus' area, (the four ends of the plus)]"
#             possible_p.append([ 5, ( (row-1,j), (row+1,j), (row,j-1), (row,j+1) ) ])



# # [5, ((0, 1), (2, 1), (1, 0), (1, 2))]
# # ...
# print(possible_p)
# print()


# for i in range(len(possible_p)):

#     plus = possible_p[i]

#     while plus is not None:

#         plus = plus_checker(plus)

#         if plus is not None:

#             possible_p[i] = plus





# possible_p.sort(key = lambda x: x[0], reverse=True)


# print(possible_p)






'plus_checker func tests cases'

    # test = [5, ((2,3), (4,3), (3,2), (3,4))]
    # grid = ['G'*(len(grid[0])+1)]*(len(grid)+1)

    # grid[1] = grid[1][:3] + 'B' + grid[1][3+1:]

    # for i in grid: print(i)

    # test = plus_checker(test)
    # print(test)

    # test = plus_checker(test)
    # print(test)

    # test = plus_checker(test)
    # print(test)

    # test = plus_checker(test)
    # print(test)

    # test = plus_checker(test)
    # print(test)







'HackerRank Output'

def plus_checker(plus):

    if plus:

        try:
            area = plus[0]
            up = plus[1][0]
            down = plus[1][1]
            left = plus[1][2]
            right = plus[1][3]

            group = ( grid[up[0]-1][up[1]], grid[down[0]+1][down[1]], grid[left[0]][left[1]-1], grid[right[0]][right[1]+1] )

            within_limits = [up[0]>0, left[1]>0, down[0]<len(grid), right[1]<len(grid[0])]

            if all(within_limits) and 'B' not in group:
                return [ area + 1,  ((up[0]-1, up[1]),  (down[0]+1, down[1]), (left[0], left[1]-1), (right[0], right[1]+1)) ] 


        except IndexError:
            return  
        

def twoPluses(grid):

    possible_p = list()

    for row in range(1, len(grid[1:-1])+1):
        
        for j in range(1, len(grid[row][1:-1])+1):

            if 'B' not in (grid[row-1][j], grid[row+1][j], grid[row][j-1], grid[row][j+1]):

                # Stored as "[Plus' area, (the four ends of the plus)]"
                possible_p.append([ 5, ( (row-1,j), (row+1,j), (row,j-1), (row,j+1) ) ])


    for i in range(len(possible_p)):

        plus = possible_p[i]

        while plus is not None:

            plus = plus_checker(plus)

            if plus is not None:

                possible_p[i] = plus


    possible_p.sort(key = lambda x: x[0], reverse=True)


    if len(possible_p) == 0:
        return 0
    
    elif len(possible_p) == 1:
        return possible_p[0][0]
    
    else:
        return possible_p[0][0]*possible_p[1][0]



print(twoPluses(grid))



'''
So far the code works, the only thing left is to check the pluses does not overlap each other

'''






"xxx"

# '-xxx- HackerRank Problem Solving Challenge done'

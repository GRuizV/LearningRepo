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




# a plus argument comes in the form "[Plus' area, (i, j)]"    being i,j the coordinates
def plus_checker(plus):

    if plus:

        try:
            area = plus[0]
            up = plus[1][0]
            down = plus[1][1]
            left = plus[1][2]
            right = plus[1][3]

            if 'B' not in ( grid[up[0]-1][up[1]], grid[down[0]+1][down[1]], grid[left[0]][left[1]-1], grid[right[0]][right[1]+1] ):

                return [ area + 1, ( (up[0]-1, up[1]), (down[0]+1, down[1]), (left[0], left[1]-1), (right[0],right[1]+1) ) ]

        except IndexError:

            return        

    

# BGBBGB
# GGGGGG
# BGBBGB
# GGGGGG
# BGBBGB
# BGBBGB

grid = ['BGBBGB', 'GGGGGG', 'BGBBGB', 'GGGGGG', 'BGBBGB', 'BGBBGB']


possible_p = list()

for row in range(1, len(grid[1:-1])+1):
    
    for j in range(1, len(grid[row][1:-1])+1):

        if 'B' not in (grid[row-1][j], grid[row+1][j], grid[row][j-1], grid[row][j+1]):

            # Stored as "[Plus' area, (the four ends of the plus)]"
            possible_p.append([ 5, ( (row-1,j), (row+1,j), (row,j-1), (row,j+1) ) ])



# # [5, ((0, 1), (2, 1), (1, 0), (1, 2))]
# ...
# print(possible_p)



'''
At this point what I am trying to do is to iterate the times the plus can go
one by one, until it hits an edge, and if its a valid plus, modify its area and coordinates
'''
for plus in possible_p:

    # This is the largest the plus can go
    limit = min(len(grid), len(grid[0]))

    # if True:

    #     plus_checker(plus)



a = ((0, 1), (2, 1), (1, 0), (1, 2))

print(min(a))





'plus_checker func tests cases'

# test = [5, ((2,3), (4,3), (3,2), (3,4))]
# grid = ['G'*(len(grid[0])+1)]*(len(grid)+1)

# # grid[0] = grid[0][:3]+'B'+grid[0][3+1:]

# # for i in grid: print(i)

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





def twoPluses(grid):
    pass








# '-xxx- HackerRank Problem Solving Challenge done'

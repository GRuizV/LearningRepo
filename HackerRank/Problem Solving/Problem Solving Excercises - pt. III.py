import math
import itertools
import collections
import random



"Ema's Supercomputer"

# # Input
# a = '''BBGGBGGBBGGGB
# BBGGBGGBBGGGB
# BBGGBGGBBGGGB
# BBGGBGGBBGGGB
# GGGGGGGGGGGGG
# BBGGBGGBBGGGB
# GGGGGGGGGGGGG
# BBGGBGGBBGGGB
# BBGGBGGBBGGGB
# GGGGGGGGGGGGG
# GGGGGGGGGGGGG
# GGGGGGGGGGGGG
# BBGGBGGBBGGGB
# GGGGGGGGGGGGG'''


# grid = [x for x in a.split('\n')]



# My solution

'1st Auxiliary Function'
# # a plus argument comes in the form "[Plus' area, (i, j)]"    being i,j the coordinates
# def plus_checker(plus):

#     if plus:

#         try:
#             area = plus[0]
#             up = plus[1][0]
#             down = plus[1][1]
#             left = plus[1][2]
#             right = plus[1][3]

#             group = ( grid[up[0]-1][up[1]], grid[down[0]+1][down[1]], grid[left[0]][left[1]-1], grid[right[0]][right[1]+1] )

#             within_limits = [up[0]>0, left[1]>0, down[0]<len(grid), right[1]<len(grid[0])]

#             if all(within_limits) and 'B' not in group:
#                 return [ area + 4,  ((up[0]-1, up[1]),  (down[0]+1, down[1]), (left[0], left[1]-1), (right[0], right[1]+1)) ] 


#         except IndexError:
#             return        



'2nd Auxiliary Function'
# # a plus argument comes in the form "[Plus' area, (i, j)]"    being i,j the coordinates
# def plus_overlap_check(pls1, pls2):

#     up1 = pls1[1][0]
#     down1 = pls1[1][1]
#     left1 = pls1[1][2]
#     right1 = pls1[1][3]

#     up2 = pls2[1][0]
#     down2 = pls2[1][1]
#     left2 = pls2[1][2]
#     right2 = pls2[1][3]

#     # This test will throw "False" when the pluses don't overlap
#     test_if_verts_meet = (up1[1] == up2[1]) and ( (up1[0] in range(up2[0], down2[0]+1)) or (down1[0] in range(up2[0], down2[0]+1)))
#     test_if_horizs_meet = (left1[0] == left2[0]) and ( (left1[1] in range(left2[1], right2[1]+1)) or (right1[1] in range(left2[1], right2[1]+1))) 
#     test_if_vrt1_meet_hrz2 = ( up1[1] in range(left2[1], down2[1]+1) ) and ( ( left1[0] in range(up2[0], down2[0]+1)) )

#     if any((test_if_verts_meet, test_if_horizs_meet, test_if_vrt1_meet_hrz2)):
#         return False
    
#     else:
#         return True



'Body of the main function'

# possible_p = list()

# for row in range(1, len(grid[1:-1])+1):
    
#     for j in range(1, len(grid[row][1:-1])+1):

#         if 'B' not in (grid[row-1][j], grid[row+1][j], grid[row][j-1], grid[row][j+1]):

#             # Stored as "[Plus' area, (the four ends of the plus)]"
#             possible_p.append([ 5, ( (row-1,j), (row+1,j), (row,j-1), (row,j+1) ) ])


# for i in range(len(possible_p)):

#     plus = possible_p[i]

#     while plus is not None:

#         plus = plus_checker(plus)

#         if plus is not None:

#             possible_p[i] = plus


# possible_p.sort(key= lambda x: x[0], reverse=True)


# for i in possible_p : print(i)
# print()


# if len(possible_p) == 0:
#     print( 0 )

# elif len(possible_p) == 1:
#     print( possible_p[0][0])

# else:
    
#     for i in range(len(possible_p)):
        
#         for j in range(len(possible_p[i+1:])):

#             if plus_overlap_check(possible_p[i], possible_p[j]) is True:

#                 print( possible_p[i][0] * possible_p[j][0])
            
#                 break
        
#         break






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




'''
My solution up to this point is 36% effective.

'''



# # Another guy's solution

# def twoPluses(grid):         
#     pluses = []  
#     for n in range(1, len(grid)-1):
#         for m in range(1, len(grid[0])-1):
#             if grid[n][m] == grid[n][m-1] == grid[n][m+1] == grid[n-1][m] == grid[n+1][m] == 'G':
#                 plus = [(n-1,m), (n,m-1), (n,m), (n,m+1), (n+1,m)]
#                 pluses.append(plus)
#                 i = 2
#                 while n+i < len(grid) and n-i >=0 and m+i < len(grid[0]) and m-i >= 0 and grid[n+i][m] == grid[n-i][m] == grid[n][m+i] == grid[n][m-i] == 'G':
#                     plus.extend([(n-i,m), (n,m-i), (n, m+i), (n+i,m)])
#                     pluses.append(sorted(plus))
#                     i += 1                
#     pluses.sort(key=lambda x: len(x), reverse=True)    
#     countG = 0
#     for row in grid:
#         countG += row.count('G') 
#     if len(pluses) == 0 and countG >= 2:
#         return 1
#     elif len(pluses) == 1:
#         if len(pluses[0]) == countG:
#             return 1
#         else:
#             return len(pluses[0])        
#     else:        
#         ans = len(pluses[0])        
#         for j,x in enumerate(pluses):
#             for y in pluses[j+1:]:
#                 for h,z in enumerate(x):
#                     if z in y:
#                         break
#                     elif h == len(x)-1 and len(x) * len(y) > ans:
#                         ans = len(x) * len(y)
#         return ans

"Solved with another guy's solution"





"xxx"

# '-xxx- HackerRank Problem Solving Challenge done'



'Problem #1'
'''
    The problem statement is how many ways are to reach to the 
    top of a trail of rocks if you can jump only 1 or 2 rocks at
    a time.

    According to chatGPT this is a fibonacci pattern, and I FUCKING HATE IT.

'''

# def fibonacci(n):

#     result = [0,1]

#     for i in range(n):
#         result.append(sum(result[-2:]))

#     return result


# print(fibonacci(7))





'Problem #2'

# def solutions(s):

#     s = s.split('-')

#     animals = [x for x in s if x != '']

#     return len(animals[-1])

# print( solutions("Elephant-Tiger-Lion-") )


# s = "-Elephant-Tiger-Lion-"

# print(s.split('-'))





'Practical Challenge'

# email_addr = 'a@g.com'



# before_at = email_addr.split('@')[0]
# after_at = email_addr.split('@')[1]


# domiain = after_at.split('.')

# print(domiain)





'''
This exercise is the one that Juan had to solve

    Given an array of integers, always woth a pair length, the task is to return the max of the sum
    of the first elements of all possible pairings within the array.
'''

# import itertools

# # Input
# s = [2,3,4,1]


# # All possible pair combinations

# pairs = list(itertools.combinations(s,2))   #[(2, 3), (2, 4), (2, 1), (3, 4), (3, 1), (4, 1)]
# # print(pairs)



# # Making all the possible combinations without repetition
# comb = []

# for i in range(len(s)-1):
    
#     for k in range(i, len(pairs)):

#         if pairs[i][0] not in pairs[k] and pairs[i][1] not in pairs[k]:

#             comb.append([pairs[i], pairs[k]])
 

# #Verifying
# print(comb) # [[(2, 3), (4, 1)], [(2, 4), (3, 1)], [(2, 1), (3, 4)]]



# # Pulling the first value of each pair to sum them
# result = []

# for elem in comb:

#     temp = []

#     for pair in elem:
#        temp.append(min(pair))
    
#     result.append(sum(temp))


# # The result should be the max of that
# print(max(result))
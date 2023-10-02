import math
import itertools


'Encryption'

# My Approach

# s = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
# # print(len(s))

# columns = math.ceil(math.sqrt(len(s)))
# # print(f'ceil: {columns}')

# rows = math.floor(math.sqrt(len(s)))
# # print(f'floor: {rows}')

# if rows * columns < len(s):
#     rows = columns

# result, rows_words = list(), list()

# for i in range(rows):
#     rows_words.append(s[i*columns:i*columns+columns])
    
# # print(rows_words)

# for i in range(columns):

#     temp = str()

#     for j in rows_words:

#         if i > len(j)-1:
#             continue
        
#         temp += j[i]
    
#     result.append(temp)

# # print(result)

# result_string = str()

# for i in result:    
#     result_string += i + ' '

# result_string.rstrip()

# print(result_string)


'''
This solution is the first draft that came to mind but I'm sure it could be a lot more efficient,
Below there is a solution that came from ChatGPT
'''

# def encryption(s):

#     s = s.replace(" ", "")  # Remove spaces
#     L = len(s)
#     R = int(math.floor(math.sqrt(L)))
#     C = int(math.ceil(math.sqrt(L)))
    
#     while R * C < L:
#         R += 1

#     grid = [['' for _ in range(C)] for _ in range(R)]

#     for i in range(L):
#         row = i // C
#         col = i % C
#         grid[row][col] = s[i]

#     encrypted_message = ""
#     for col in range(C):
#         for row in range(R):
#             if grid[row][col] != '':
#                 encrypted_message += grid[row][col]
#         encrypted_message += " "  # Add space between columns

#     return encrypted_message

# # Example usage:
# input_string = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
# result = encryption(input_string)
# print(result)




'Bigger is Greater'


# w = 'dkhc'


# # Base solution
# comb = list(map(list, itertools.permutations(w)))
# comb = list(map(''.join,comb))

# comb.sort(reverse=True)
# ind = comb.index(w)
# result = comb[ind-1]

# print(comb)
# print(len(comb))
# print(result)


# # Solution sent to HackerRank
# def biggerIsGreater(w):
    
#     comb = list(map(list,itertools.permutations(w)))
#     comb = list(map(''.join,comb))
#     comb.sort(reverse=True)
#     ind = comb.index(w)
#     result = comb[ind-1]
    
#     if ind == 0 or result == w:
#         return 'no answer'
    
#     return result

''' 
This solution evidently is based on brute force,
3 out of the 5 cases failed due to time limit excedeed or runtime error,

    Pending: needs optimization.
'''


# ChatGPT's Solution

'''
According to ChatGPT here, the optimal solution which will be O(n), is to find the inmediate next permutation bigger
by finding the first pair (a,b) where a > b within the characters in the string, then find the rightmost character (c) which satisfies c > a, and then
swap those two and reverse that part of the string
'''

# def biggerIsGreater(w):
    
#     w = list(w)

#     i = len(w) - 2

#     while i >= 0 and w[i] >= w[i + 1]:
#         i -= 1

#     if i == -1:
#         return 'no answer'    


#     j = len(w) - 1

#     while w[j] <= w[i]:
#         j -= 1

#     w[i], w[j] = w[j], w[i]


#     w[i + 1:] = reversed(w[i + 1:])

#     return ''.join(w)

# print(biggerIsGreater(w))

'''
Done!
'''




'Modified Kaprekar Numbers'


# # My Solution
# p = 1
# q = 100

# rang = range(p,q+1)

# kapr_nums = list()

# for i in rang:

#     d = len(str(i))

#     pow2 = pow(i,2)
#     pow2 = str(pow2)
#     r = pow2[-d:]
#     l = pow2[:-d]

#     if l != '':
#         l,r = int(l),int(r) 
    
#     else:
#         l,r = 0, int(r)

#     if r + l == i:
#         kapr_nums.append(i)
        
# print(kapr_nums)


'''
My solution worked just fine, but I am curious if there was another way to do it without brut forcing it

    Note: After reviewing the discussion board and ChatGPTs opinion, all the solutions converge in the same solution.
'''




'Beutiful triplets'


# arr = [1, 2, 4, 5, 7, 8, 10]
# arr = [2,2,3,4,5]
# d = 3

# # First approach
# triplets = list(itertools.combinations(arr,3))

# b_triplets = list()

# for i in triplets:

#     if i[2] - i[1] == i[1] - i[0] == 3:
#         b_triplets.append(i)

# print(b_triplets)

'Brute forcing it wont do, Ill try somehting different'


# # Second approach
# b_triplets = list()

# for i in range(len(arr) - 2):

#     triplet = list()
#     triplet.append(arr[i])
    
#     for j in range(i+1, (len(arr)-2) + 1):

#         if arr[j] - arr[i] == d:
#             triplet.append(arr[j])

#             for k in range(j+1, len(arr)):

#                 if arr[k] - arr[j] == d:

#                     triplet.append(arr[k])
#                     b_triplets.append(triplet)
#                     triplet = triplet[:-1]
            
#             triplet = triplet[:-1]
  
# print(b_triplets)

'This second approach worked perfectly'




'xxx'
































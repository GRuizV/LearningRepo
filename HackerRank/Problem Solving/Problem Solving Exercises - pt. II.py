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




'xxx'




















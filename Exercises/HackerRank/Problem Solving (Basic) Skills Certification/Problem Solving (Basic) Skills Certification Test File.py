'1. Username changes'

# input

# case1
# users = ['hydra']

# case2
# users = ['foo', 'bar', 'baz']

# Custom Case
# users = []


# My approach
# def possibleChanges(usernames: list[str]) -> list[str]:

#     res = []

#     for username in usernames:

#         if len(username) <= 1:
#             res.append('NO')
        
#         else:
#             new_username = ''.join(sorted(username))

#             if username[0] == new_username[0]:
#                 res.append('NO')
            
#             else:
#                 res.append('YES')

#     return res



# sol = possibleChanges(users)
# print(sol)

'''
Notes:
    Apparently, it worked. Only thing that eluded me was a single character username cornercase.
'''




'2. Password Decryption'

# input

# case1
# s = '51Pa*0Lp*0e'   # Expected output: 'aP1pL5e'

# case2
# s = 'pTo*Ta*O'   # Expected output: 'poTaTO'

# Custom Case
# s = ''


# My approach
# def decryptPassword(s:str) -> str:

#     while True:
        
#         if s.find('*') != -1:
            
#             idx = s.find('*')

#             s = s[:idx-2] + s[idx-1] + s[idx-2] + s[idx+1:]

#         else:

#             zero_count = s.count('0')
#             numbers = s[:zero_count]
#             numbers = numbers[::-1]
#             s = s[zero_count:]

#             for i in range(zero_count):
                
#                 idx = s.find('0')
#                 s = s[:idx] + numbers[i] + s[idx+1:]

#         if '*' not in s and '0' not in s:
#             break

#     return s
                
# print(decryptPassword(s))

'''
Notes:
    Apparently, it worked.
'''
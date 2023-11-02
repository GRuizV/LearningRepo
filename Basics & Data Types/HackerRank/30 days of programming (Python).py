'''
Day 8: Dictionaries and Maps
'''


'''
Task

Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. 
For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for  is not found, print Not found instead.


input

... After the  lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.


'''


# N = int(input().strip())

# d = dict()

# for i in range(N):

#     inp = input().strip().split()

#     d[inp[0]] = inp[1]



# while True:

#     try:

#         name = input().strip()

#         inp = d.get(name,'Not found')

#         if inp == 'Not found':
#             print(inp)
        
#         else:
#             print(f'{name}={d[name]}')

#     except EOFError:
#         break




'''
Day 10: Binary Numbers
'''

# # 125 

# n = 60907

# n_bin = bin(n)

# print(n_bin)
# print(len(n_bin))

# s = sorted(str(n_bin[2:]).split('0'))

# print(s)




_ = 'Day 20: Sorting'


# l = [4,3,1,2]


# swapped = True
# counter = 0

# while swapped is not False:

#     swapped = False

    

#     i = 0

#     while True:

#         if i == len(l)-1:
#             break

#         if l[i] > l[i+1]:

#             l[i], l[i+1] = l[i+1], l[i]

#             swapped = True

#             counter += 1

#         i += 1


# print(l)
# print(counter)




_ = 'Day 25: Running Time and Complexity'



'My Solution'

# def primes(n):

#     primes = [1]
#     non_primes = list()

#     for i in range(2,n+1):

#         if i not in non_primes:

#             primes.append(i)

#             for j in range(i*i, n+1, i):

#                 non_primes.append(j)

#     return primes


# l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 907]

# n = max(l)
# primes_n = primes(n)

# res = list()

# for i in l:

#     if i in primes_n and i!=1:
#         res.append('Prime')
    
#     else:
#         res.append('Not prime')

# print(res)


'----------------------------------------------------------------------'


'Another Guys solution'
# This solution is way scalable than the one with erasthotene's sieve
# Since it reduces the numbers to check prime


# import math

# t = int(input())

# def isPrime(n):
    
#     if n==1: return 'Not prime'
    
#     for i in range(2,int(math.sqrt(n))+1):
        
#         if n%i==0:
#             return 'Not prime'
            
#     return 'Prime'
    
    
# for i in range(t):
    
#     n = int(input())
    
#     print(isPrime(n))




_ = 'Day 26: Nested Logic'


# fine = 0

# ret = [23, 12, 1234]
# due = [19, 9, 2468]


# if ret[2] > due[2]:

#     fine = 10000

# elif ret[1] > due[1] and ret[2] == due[2] :

#     fine = 500*(ret[1]-due[1])

# elif ret[0] > due[0] and ret[1] == due[1] and ret[2] == due[2]:

#     fine = 15*(ret[0]-due[0])


# print(fine)















"1. Sum up of digits"

'''
    Write a recursive function to calculate the sum of digits in a positive integer. 
    For example, the sum of digits in 12345 is 1+2+3+4+5 = 15.
'''

# Input
# n = '12345'


"My approach"
# def sum_of_digits(n, end):

#     if n == end:
#         return int(n)

#     return int(n[0]) + sum_of_digits(n[1:], end)


# end = n[-1]
# result = sum_of_digits(n, end)

# print(result)   #Expected result: 15, for n = '12345'



"ChatGPT's Solution"
# def sum_of_digits(n):

#     if len(n) == 1:
#         return int(n)

#     return int(n[0]) + sum_of_digits(n[1:])


# result = sum_of_digits(n)

# print(result)   #Expected result: 15, for n = '12345'

'I was this close... but fair enough!'






"2. Greatest Common Divisor"

'''
    Write a recursive function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm. 
    The GCD of two integers is the largest positive integer that divides both of them.

    The Euclidean algorithm is defined as follows:

        gcd(a, b) = a, if b == 0
        gcd(a, b) = gcd(b, a % b), otherwise


'''

"My approach"

# # Auxiliary primes function
# def primes(num):

#     primes = [1]
#     not_primes = list()

#     for i in range(2, num+1):

#         if i not in not_primes:
#             primes.append(i)

#         for j in range(i+i, num+1, i):
#             not_primes.append(j)

#     return primes


# # First I will try to do it without recursion, then I'll figure out the recursive version
# def nr_gcd(a, b):

#     if a == 0 or b == 0:        
#         return a if b == 0 else b

#     num = min(a, b)

#     num_gcd = set()

#     while num != 1:

#         num_primes = primes(num)[1::]

#         for i in num_primes:

#             if num % i == 0:
#                 num_gcd.add(num//i)
#                 num //= i
#                 break
    
#     num_gcd = sorted(num_gcd, reverse = True)
#     num_gcd.insert(0, b)       

#     num = max(a, b)

#     for div in num_gcd:

#         if num % div == 0:

#             return div    


# print(nr_gcd(48,18))

"I think I'm done with this exercise"



"Chat GPT's Solution"

# def gcd(a,b):

#     if b == 0:
#         return a
    
#     return gcd(b, a % b)

# a = 48
# b = 18

# print(gcd(a,b))





"3. Write a Python program to sum recursion lists."

'''
Test Data: [1, 2, [3, 4], [5, 6]]
Expected Result: 21
'''

"Page's Solution"

def rec_sum(lst):
   
    total = 0

    for element in lst:

        if isinstance(element, list):
            total += rec_sum(element)
        
        else:
            total += element
        
    return total    




data = [1, 2, [3, 4], [5, 6]]

print(rec_sum(data))





# '-xxx- Recursion Challenge Done!'
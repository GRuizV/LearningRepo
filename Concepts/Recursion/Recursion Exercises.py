

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



# '-xxx- Recursion Challenge Done!'
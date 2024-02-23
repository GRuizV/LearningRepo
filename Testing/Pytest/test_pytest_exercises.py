'source: https://www.w3resource.com/python-exercises/unittest/index.php'
# path: 'C:\Users\USUARIO\GR\Software Development\Learning\Testing\Pytest'

import pytest


'1. Write a Python unit test program to check if a given number is prime or not.'

# # Defining the Function
# def isprime(n):

#     primes = [1]
#     non_primes = []

#     for i in range(2, n+1):

#         if i not in non_primes:

#             primes.append(i)
#             [non_primes.append(num) for num in range(i*i, n+1, i)]

#     return n in primes



# # Testing primes numbers
# def test_prime_numbers():

#     primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#     print(f'Prime numbers: {primes}')

#     for prime in primes:
#         assert isprime(prime) == True



# # Testing non primes numbers
# def test_non_prime_numbers():

#     non_primes = [4, 6, 8, 10, 12, 14, 16, 18, 20]
#     print(f'Prime numbers: {non_primes}')

#     for non_prime in non_primes:
#         assert isprime(non_prime) == False




'2. Write a Python unit test program to check if a list is sorted in ascending order.'


# def list_in_ascending_order(li):

#     check = []

#     for i in range(1, len(li)):
#         check.append(li[i]>=li[i-1])

#     return all(check)


# def test_list_in_ascending_order():

#     li = [0,1,2,3,4,5,6]
#     assert list_in_ascending_order(li) == True


# def test_list_not_in_ascending_order():

#     li = [0,1,2,8,4,5,6]
#     assert list_in_ascending_order(li) == False




'3. Write a Python unit test program that checks if two lists are equal.'


'4. Write a Python unit test program to check if a string is a palindrome.'


'5. Write a Python unit test program to check if a file exists in a specified directory.'


'6. Write a Python unit test that checks if a function handles floating-point calculations accurately.'


'7. Write a Python unit test program to check if a function handles multi-threading correctly.'


'8. Write a Python unit test program to check if a database connection is successful.'


'9. Write a Python unit test program to check if a database query returns the expected results.'


'10. Write a Python unit test program to check if a function correctly parses and validates input data.'
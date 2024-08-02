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

# def equal_lists(li1, li2):

#     return li1 == li2


# def test_if_are_equal():

#     dummy1 = [1,2,3,4]
#     dummy2 = [1,2,3,4]

#     assert equal_lists(dummy1, dummy2)

# @pytest.mark.xfail
# def test_if_are_not_equal():

#     dummy1 = [1,2,3,4]
#     dummy2 = [1,2,3,5]

#     assert equal_lists(dummy1, dummy2)



'4. Write a Python unit test program to check if a string is a palindrome.'

# def ispalindrome(s):
#     return s == s[::-1]


# def test_if_palindrome():

#     s = 'eye'

#     assert ispalindrome(s)


# @pytest.mark.xfail
# def test_if_not_palindrome():

#     s = 'ball'

#     assert ispalindrome(s)



'5. Write a Python unit test program to check if a file exists in a specified directory.'

# import os

# def file_exists(directory:str, file_name:str) -> True | False:

#     file_path = os.path.join(directory, file_name)

#     return os.path.exists(file_path)

# # print(file_exists(r'C:\Users\USUARIO\GR\Software Development\Learning\Testing\Pytest', 'test_pytest_exercises.py'))


# def test_if_file_exists():

#     directory = r'C:\Users\USUARIO\GR\Software Development\Learning\Testing\Pytest'
#     file_name = 'test_pytest_exercises.py'

#     assert file_exists(directory, file_name)

# @pytest.mark.xfail
# def test_if_file_not_exists():

#     directory = r'C:\Users\USUARIO\GR\Software Development\Learning\Testing\Pytest'
#     file_name = 'foo.py'

#     assert file_exists(directory, file_name)



'6. Write a Python unit test that checks if a function handles floating-point calculations accurately.'

# def floating_sum(num1:float, num2:float) -> float:
#     return round(num1 + num2, 5)


# def test_floating_sum():

#     n1 = 0.15
#     n2 = 0.2224
    
#     assert n1 + n2 == floating_sum(n1, n2)



'7. Write a Python unit test program to check if a function handles multi-threading correctly.'

# import threading

# # Define a function 'perform_task' that simulates some computational task.
# def perform_task():

#     # Initialize a result variable.
#     result = 0

#     # Simulate a task by summing numbers from 1 to 99999.
#     for i in range(1, 100000):
#         result += i

#     # Return the result of the task.
#     return result


# def test_multi_threading():

#     # Define the number of threads to create
#     num_threads = 10

#     # Create a list to hold the threads
#     threads = []

#     # Create and Start the Threads

#     for _ in range(num_threads):

#         # Create a thread, specifying the target function 'perform_task'
#         t = threading.Thread(target=perform_task)

#         # Append the thread to the 'threads' list
#         threads.append(t)

#         # Start the thread execution
#         t.start()

#     # Wait for all the threads to finish
#     for t in threads:
#         t.join()

#     for t in threads:
#         assert not t.is_alive() # is_alive() returns True if a thread is not finished its job


'8. Write a Python unit test program to check if a database connection is successful.'

# import sqlite3

# # Create a function that will create a database connection in memory
# def database_connection():

#     conn = sqlite3.connect(':memory:')

#     # Create a cursor to interact with the database
#     cursor = conn.cursor()

#     # Execute a simple query to select the value 1
#     cursor.execute("SELECT 1")

#     # Fetch the result of the query
#     result = cursor.fetchone()

#     # Close the cursor and the database connection
#     cursor.close()
#     conn.close()

#     return result
    


# def test_database_connection():

#     result = database_connection()

#     assert result == (1,)



'9. Write a Python unit test program to check if a database query returns the expected results.'

# import sqlite3

# # Define a method 'setUp' that is executed before each test.
# def setUp():

#     # Create a database connection in memory and insert test data.
#     conn = sqlite3.connect(':memory:')
#     cursor = conn.cursor()

#     # Create an 'employees' table and insert test records.
#     cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
#     cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ylva Guiomar', 1800.0)")
#     cursor.execute("INSERT INTO employees (name, salary) VALUES ('Scott Gregorius', 2100.0)")
#     conn.commit()

#     return conn, cursor

# # Define a method 'tearDown' that is executed after each test.
# def tearDown(cursor, conn):

#     # Close the database cursor and the database connection.
#     cursor.close()
#     conn.close()


# # Define a test method 'test_database_query' to test a database query.
# def test_database_query():

#     set_up_res = setUp() 

#     cursor = set_up_res[1]

#     # Execute a SQL query to select employee names and salaries, ordered by name.
#     cursor.execute("SELECT name, salary FROM employees ORDER BY name")
#     results = cursor.fetchall()

#     # Define the expected results as a list of tuples.
#     expected_results = [('Scott Gregorius', 2100.0), ('Ylva Guiomar', 1800.0)]

#     # Assert that the results match the expected results.
#     assert results == expected_results





'10. Write a Python unit test program to check if a function correctly parses and validates input data.'

# # This will validate an input of only numeric input
# def parse_and_validate_numeric_input(data):

#     if isinstance(data, str) and data.isnumeric():
#         return True

#     return False


# # This will validate an input of only numeric input
# def parse_and_validate_alphabetic_input(data):

#     if isinstance(data, str) and data.isalpha():
#         return True

#     return False



# def test_valid_numeric_input():

#     data = '100'

#     assert parse_and_validate_numeric_input(data)


# @pytest.mark.xfail
# def test_invalid_numeric_input():

#     data = 'Hello'

#     assert parse_and_validate_numeric_input(data)
    

# def test_valid_alphabetic_input():

#     data = 'Hello'

#     assert parse_and_validate_alphabetic_input(data)


# @pytest.mark.xfail
# def test_invalid_alphabetic_input():

#     data = '100'

#     assert parse_and_validate_alphabetic_input(data)
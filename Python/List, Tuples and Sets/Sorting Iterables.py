import math
from fractions import Fraction as F
from decimal import Decimal as D
import random


# li = [1, -2, 15, -78, math.pi, 100, D(4/3)]

# li= sorted(li, key = abs, reverse = False)

# print(li)





# li = "This is a Test to check how Sorted() function works"

# li = sorted(li, key = str.lower, reverse = True)

# print(li)




# li = [ [random.randint(1, 5) for x in range(5)], [random.randint(1, 5) for x in range(5)], [random.randint(1, 5) for x in range(5)]]

# print(li)

# for i in li:
#     i.sort()

# print(li)

# li = sorted(li, reverse=False)

# print(li)





# from operator import attrgetter

# class Employee():

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def __repr__(self):
#         # return 'f({self.name}, {self.age}, {self.salary})'  # Apparently fStrings doesn't work here
#         return '({}, {}, ${})'.format(self.name, self.age, self.salary)


# e1 = Employee('Juan', 30, 30000)
# e2 = Employee('Jerry', 29, 0)
# e3 = Employee('Vic', 31, 7000)

# employees = [e1, e2, e3]

# # def e_sort(emp):
# #     return emp.salary

# s_employees = sorted(employees, key = attrgetter('age'), reverse = True)

# print(s_employees)


'''
Dictionaries fundamentals
'''

# print(dir(dict))

# student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# # get() method
# print(student.get('phone', "Not Found!")) 

# # update() method
# student.update({'name': 'Gerardo', 'age': 29, 'courses': ['Arts', 'Socials'], 'gender' : "men"})

# print(student)

# # Removing an item with the del statement
# del student['gender']

# print(student)

# # len() on a dictionary
# print(len(student))

# # Looping thru the dict
# for elem in student:
#     print (elem)

# for key, value in student.items():
#     print(key, value)


# # Casting list() into a dictionary
# print(list(student))


# # .fromkeys() method
# li = ['a', 'b', 'c']

# val = ['x']

# new_dict = dict.fromkeys(li, val)

# print(new_dict)

# val.append('y')

# print(new_dict)



# # setfefault() method
# person = {'name': 'Phill', 'age': 22}

# print(person.setdefault('name'))

# print(person.setdefault('Gender', 'Men'), person)

# print(person.setdefault('Sign'), person)



'''DictComp'''

# letters = ['A', 'B', 'C', 'D', 'E']
# numbers = [100, 550, 948, 95, 12]

# dict1 = { letter : number for letter, number in zip(letters, numbers)  }    #Simple DictComp to build the dict

# print(dict1)

# sorted_dict = { k: v for k, v in sorted( dict1.items(), key = lambda x: x[1], reverse = False ) }   #DictComp to order the dict

# print(sorted_dict)




'''
OrderedDict()
'''

# from collections import OrderedDict

# # Setting variables

# reg_d = {'a': 1, 'b': 2, 'c': 3}

# reg_p = {'c': 3, 'a': 1, 'b': 2}

# d = OrderedDict()

# d['a'] = 1
# d['b'] = 2
# d['c'] = 3

# p = OrderedDict()

# p['c'] = 3
# p['a'] = 1
# p['b'] = 2


# # popitem()

# print(reg_d)

# pop_rd = reg_d.popitem()

# print(pop_rd, reg_d)


# print(d)

# pop_d = d.popitem(last=False)

# print(pop_d, d)



# # move_to_end()

# print(d)

# d.move_to_end('b', last=True)

# print(d)

# d.move_to_end('b', last=False)

# print(d)



# Comparing dicts and OrderDicts

# print(reg_d == reg_p)

# print(d == p)
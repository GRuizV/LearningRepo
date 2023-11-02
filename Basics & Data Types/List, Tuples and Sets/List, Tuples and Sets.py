'''
LISTS
'''

# l = ['A', 'B', 'C', 'D', 'F', 'R', 'C']

# l2 = list(enumerate(l))

# print(l2)

# for i, v in l2:
#     print(l2[i][-1])

# l.insert(0, 'E')

# print(l)


# l3 = [ [ ['alpha', 'beta'], 'gamma' ], [ 'mu', ['omicron'] ] ]

# print(l3[0][0][0])



# print(l.index('C', 3, 7))

# a = l.copy()

# print(a)



'''
    the del statement
'''

# a = [-1, 1, 66.25, 333, 333, 1234.5]

# del a[0]
# print(a)

# del a[2:4]
# print(a)

# del a[:]
# print(a)



'''
itertools.zip:longest()
'''

# from itertools import zip_longest

# iter1 = ['A', 'B', 'C', 'D', 'E']
# iter2 = ['x', 'y', 'z']
# iter3 = [1, 2, 3]

# iter4 = list(zip_longest(iter1, iter2, iter3, fillvalue=None))

# print(iter4)





'''
TUPLES
'''

# l = ['A', 'B', 'C', 'D', 'F', 'R', 'C']

# l2 = l

# print(f'{l}\n{l2}')

# l[0] = '7'

# print(f'{l}\n{l2}')


# l2 = tuple(l)

# l[0] = '7'

# print(f'{l}\n{l2}')


# my_tuple = ('word', 114, True)

# print(my_tuple)

# a, b, c = my_tuple

# print(a)
# print(b)
# print(c)


# l = (1, 1, 1, 2, 3, 1, 5)

# print(l.index(1,3))


''' ----------- '''

# tuple1 = (1, 2, 3, 4)

# # Merging tuples

# tuple1 = tuple1 + (9,)

# print(tuple1)


# # Subtracting tuples

# tuple1 = tuple1[:-1]

# print(tuple1)


# # Adding items in the middle of the tuple

# tuple1 = tuple1[:2] + ('A', 'B', 'C') + tuple1[2:]

# print(tuple1)



''' ----------- '''

# Tuples comprehension

# l = [ x for x in range(5) ]

# print(l)

# t = ( x for x in l ) # Not a tuple, but a generator object instead

# print(t)



'''
    Named Tuples
    
'''

# from collections import namedtuple


# # Declaring the namedtuple()
# Student = namedtuple('Student', ['name', 'age', 'ID'])


# # Adding values
# S = Student('Gerardo', 29, '3934')


# # Accessing using index
# print(f"The Student age using index is : {S[1]}")


# # Accessing using an attribute
# print(f"The Student name using keyname is : {S.name}")


# # It also supports the getattr()
# print(f"The Student ID using getattr() is : {getattr(S, 'ID')}")



''' ----------- '''

 
# # Using the _make(), _asdict() and ** operator

# # initializing an iterable
# li = ['Juan', 30, '7825']

# # using _make() to return namedtuple()
# print(f'The namedtuple instance using iterable is : {Student._make(li)}')

# # using _asdict() to return an OrderedDict()
# print(f'The OrderedDict instance using namedtuple is : {S._asdict()}')

# # initializing dictionary
# di = {'name':'Juan', 'age': 30, 'ID': '7825'}

# # using ** operator to return namedtuple from dictionary
# print(f'The namedtuple instance from dict is : {Student(**di)}')


''' ----------- '''


# # # Additional operations: _fields and _replace()

# # Using _field attribute to display all the keynames of the namedtuple()
# print(f'All the field of students are : {S._fields}')


# # Using _replace() to it would create a new namedtuple and will leave the original intact
# print('returns a new namedtuple :') 
# print(S._replace( name = 'Juan'))

# # Original namedtuple instance
# print(S) 




'''
SETS
'''

# print(dir(set))

# from timeit import default_timer as timer
# import random
# import string as str


''' Tests to check membership '''

# list1 = []

# for i in range(100000):
#     list1.append(random.randint(1,100000))


# set1 = set(list1)


# start = timer()
# if 8 in list1: print('Found!') 
# else: print('Not Found!')
# end = timer()

# print(end-start)


# start = timer()
# if 8 in set1: print('Found!') 
# else: print('Not Found!')
# end = timer()

# print(end-start)

# print(len(list1))
# print(len(set1))

# # This was a test to check if sets were better to check membership than lists.


''' ---------- '''


# # second test with identical data but different datatype.

# list2 = [x for x in str.ascii_letters]

# set2 = set(list2)

# start = timer()
# if 8 in list2: print('Found!') 
# else: print('Not Found!')
# end = timer()

# print(end-start)


# start = timer()
# if 8 in set2: print('Found!') 
# else: print('Not Found!')
# end = timer()

# print(end-start)

''' The result is conclusive, sets do this twice better than lists.'''





''' ----------- '''

# # Empty Sets creation

# set1 = {} #this creates an empty dictionary
# print(type(set1))

# set2 = set()
# print(type(set2))



''' ----------- '''

# #Sets Comprehensions

# set3 = {random.randint(1,20) for i in range(20) }

# print(f'{len(set3)}\n',set3)




'''
    Set's methods
'''


# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Chemistry', 'Art'}


# print(cs_courses.intersection(art_courses))

# cs_courses.intersection_update(art_courses)

# print(cs_courses)


# new_set = cs_courses.intersection_update(art_courses)

# print(new_set)


# print(cs_courses.difference(art_courses))

# cs_courses.difference_update(art_courses)

# print(cs_courses)


# new_set = cs_courses.difference_update(art_courses)

# print(new_set)



# print(cs_courses.symmetric_difference(art_courses))



# print(cs_courses.union(art_courses))



# cs_courses = cs_courses.add('Literature')

# print(cs_courses)



# new_set = set().add('element')

# print(new_set)



# cs_courses.clear()

# print(cs_courses)



# cs_courses.discard('Math')

# print(cs_courses)

# new_set = cs_courses.discard('Math')

# print(new_set)



# new_set = {'a', 'b', 'c', 'd', 'e'}

# new_list = ['e', 'f', 'g', 'h']

# dict1 = {'a' : 1, 'f' : 2, 'h' : 4}

# dict2 = {1 :'a', 2 : 'f'}

# print(f'{new_set.isdisjoint(new_list)}')
# print(f'{new_set.isdisjoint(dict1)}')
# print(f'{new_set.isdisjoint(dict2)}')



# set1 = {'a', 'b', 'c', 'd', 'e'}

# set2 = {'b', 'c'}

# list1 = {'b', 'c'}

# dict1 = {'b' : 1, 'c' : 2}

# list2 = list(dict1)

# print(set2.issubset(set1))
# print(set2.issubset(list1))
# print(set2.issubset(dict1))


# print(set1.issuperset(set2))
# print(set1.issuperset(list1))
# print(set2.issuperset(set1))


# print(set1.pop())
# print(set1)

# print(set().pop())


# new_set = set1.remove('b')
# print(new_set)

# set1.remove('a')
# print(set1)





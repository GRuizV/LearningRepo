'''
1. Write a Python script to sort (ascending and descending) a dictionary by value.

'''

# d = {'d': 0, 'a': 2, 'b': 4, 'e': 3, 'c': 1 }

# print(f'Original dict: {d}')


''' ------------ '''

# # Thru looping

# l = [ x for x in d.items() ]


# # My version of the sorting algorithm
# for i in range( len(l) - 1 ):

#     li = [ x[1] for x in l[ i - len(l) : ] ]

#     ind = li.index( min( li ) ) + i

#     if l[i][1] > l[ind][1]:

#         l[i], l[ind] = l[ind], l[i]


# res = { x[0]: x[1] for x in l }
           
# print(f'Ordered dict: {res}')


''' ------------ '''


# # Thru sorted()

# res = dict(sorted( d.items(), key = lambda x: x[1] , reverse = False ) )

# print(f'Ordered dict: {res}')



'''
3. Write a Python script to concatenate the following dictionaries to create a new one. Go to the editor

    Sample Dictionary :

    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}


    Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

'''

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}

# res = dict()

# for dic in dic1, dic2, dic3: res.update(dic)

# print(res)





'''
6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 


    Sample Dictionary ( n = 5) :
    Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''

# n = 5

# res = { x: x**2 for x in range(1, n+1) }

# print(res)




'''
10. Write a Python program to sum all the items in a dictionary.

'''

# dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# res = sum(dict1.values())

# res = sum( [ y for x,y in dict1.items() ] )

# print(res)




'''
11. Write a Python program to multiply all the items in a dictionary.

'''
# import math

# dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# res = math.prod(dict1.values())
# print(res)


# res = 1

# for k, v in dict1.items(): res *= v

# print(res)




'''
13. Write a Python program to map two lists into a dictionary

'''

# l1 = list('ABCDE')

# l2 = list(map(int,'12345'))

# res = { let: num for let, num in zip(l1, l2) }
# print(res)


# res = dict(zip(l1,l2))
# print(res)




'''
17. Write a Python program to remove duplicates from the dictionary.

'''


# student_data = {
    
#     'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },

#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },

#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },

#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }


# # Looping solution

# res = dict()

# for i in student_data:

#     if student_data[i] in res.values(): continue

#     res[i] = student_data[i]


# print(res)




'''
19. Write a Python program to combine two dictionary by adding values for common keys.

    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}

    Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

'''

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}


''' ---------- '''

# # My approach

# # indexing all items of both dicts
# elements = list( map( list, (d1.items(), d2.items()) ) )

# # Flattening the list
# elements = [ item for elem in elements for item in elem ]

# print(elements)

# res = dict()

# for i in range(len(elements)):

#     if elements[i][0] in res.keys():

#         res[ elements[i][0] ] += elements[i][1]

#     else: res[ elements[i][0] ] = elements[i][1]

# print(res)




''' ---------- '''

# # Page's approach with Counter from Collections

# from collections import Counter

# res = Counter(d1) + Counter(d2)

# print(res)





'''
20. Write a Python program to print all distinct values in a dictionary.

    Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

    Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''

# base = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]


''' ---------- '''

# # My setcomp approach

# res = { v for item in base for v in item.values() }

# print(res)



''' ---------- '''

# # Looping approach

# res = set()

# for elem in base:

#     res.add(list(elem.values())[0])

# print(res)





'''
21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

    Sample data : {'1':['a','b'], '2':['c','d']}

    Expected Output:
    ac
    ad
    bc
    bd
    
'''

# d = {'1':['a','b'], '2':['c','d']}

''' ------------- '''

# # My Approach

# res = [ [v[0], v[1]] for v in d.values() ]

# li = list()

# for i in range( len(res) - 1 ):

#     for j in range( len(res[i]) ):

#         for k in range( i+1, len(res) ):

#             for l in range( len(res[k]) ):

#                 print(f'{res[i][j]}{res[k][l]}')   
             
       


''' ------------- '''

# # Page's Approach importing itertools

# import itertools      

# d ={'1':['a','b'], '2':['c','d']}

# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):

#     print(''.join(combo))





'''
22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

    Sample data : 
    my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  

    Expected Output:
        ['b', 'e', 'c']
    
'''


# d = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  

# res = [ k for k,v in sorted(d.items(), key = lambda x: x[1], reverse = True) ]

# print(res[:3])





'''
23. Write a Python program to combine values in a list of dictionaries.

    Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

    Expected Output: {'item1': 1150, 'item2': 300}
    
'''

# l = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# d = dict()

# for dic in l:

#     if dic['item'] in d.keys():

#         d[dic['item']] += dic['amount']
    
#     else: 
        
#         d[dic['item']] = dic['amount']


# print(d)





'''
24. Write a Python program to create a dictionary from a string. 

    Note: Track the count of the letters from the string.

    Sample string : 'w3resource'

    Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
    
'''

# s = 'w3resource'


''' ------------ '''

# # Thru looping

# d = dict()

# for i in s:

#     if i in d.keys():

#          d[i] += s.count(i)

#     d[i] = s.count(i)

# print(d)



''' ------------ '''

# # Thru dictComp

# d = { k : s.count(k) for k in set(s) }

# print(d)





'''
25. Write a Python program to print a dictionary in table format. 

    Note: Track the count of the letters from the string.

    Sample: {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

    Expected output: 

    C1 C2 C3                                                                                                      
    1 5 9                                                                                                         
    2 6 10                                                                                                        
    3 7 11
    
'''

# d = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}


''' ------------- '''


# # My Approach

# res = list()

# res.append( list(d.keys()) )

# res.extend( list( map( list, zip(*d.values()) ) ) )


# for i in res:

#     # print(i)

#     for j in i:

#         print(f'{j:<2} ', end="")
        
#     print()



''' ------------- '''

# # Page's Approach

# print(  * ( [key] + value for key, value in sorted( d.items() ) ) )    # This kind of approach is recurring to generators which I don't know yet

# # print ( list( zip( * ( [key] + value for key, value in sorted( d.items() ) ) ) ) )





'''
27. Write a Python program to convert a list into a nested dictionary of keys.

    Sample: 
    
    l = ['A', 'B', 'C', 'D', 'E']

    Expected Output: {1: {2: {3: {4: {}}}}}
      
'''

# l = ['A', 'B', 'C', 'D', 'E']

# new_dict = d = dict()

# for k in l:

#     d[k] = {}

#     d = d[k]
        
# print(new_dict)


# # This is the solution proposed by the page, but tbh I didn't end to understand it.





'''
37. Write a Python program to replace dictionary values with their sums.

    Sample:

    student_details= [
    {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
    {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
    {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
    ]       

    
    Expected Output: 

    [ {'subject': 'math', 'id': 1, 'V+VI': 76.0}, {'subject': 'math', 'id': 2, 'V+VI': 73.5}, {'subject': 'math', 'id': 3, 'V+VI': 80.5} ]
    
'''


# student_details= [
#     {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#     {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#     {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
#     ] 


# for dic in student_details:

#     dic['V+VI'] = (dic['V'] + dic['VI'])/2
#     del dic['V'], dic['VI']


# print(student_details)





'''
38. Write a Python program to match key values in two dictionaries.

    Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}

    Expected output: key1: 1 is present in both x and y
    
'''


# d1, d2 = {'key1': 1, 'key5': 3, 'key3': 2}, {'key1': 1, 'key2': 2}

# res = [ print(f'{k} present in both dictionaries') for k in d1.keys() if k in d2.keys() ]

# if len(res) == 0: print('No common keys between dictionaries')





'''
40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. 
    Access the fifth value of each key from the dictionary. 

     
    Expected output:

    {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
    'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
    'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

    15
    25
    35
    
    x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
    y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
    z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
    
'''

# d = { i[0]: [10*(i[1]) + j for j in range(10)] for i in [('x',1),('y',2),('z',3)] }


# [print(i) for i in d.items()]


# for i in d:
#     print(d[i][5])


# [print(f'{i[0]} has value {i[1]}') for i in d.items()]





'''
42. Write a Python program to filter a dictionary based on values.

    Original Dictionary:
    {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    Marks greater than 170:
    {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    
'''

# d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

# res = { k : v for k,v in d.items() if v > 170 }

# print(res)





'''
43. Write a Python program to convert more than one list to a nested dictionary.

    Original strings:
    ['S001', 'S002', 'S003', 'S004']
    ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
    [85, 98, 89, 92]


    Nested dictionary:
    [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
    
'''

# l1 = ['S001', 'S002', 'S003', 'S004']

# l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']

# l3 = [85, 98, 89, 92]


''' ---------- '''

# My approach

# res = [  { i : n } for i, n in zip(l1, [ { j : k } for j, k in zip(l2, l3) ] )   ]        # This is the oneliner version of my solution.

# # [{'Adina Park': 85}, {'Leyton Marsh': 98}, {'Duncan Boyle': 89}, {'Saim Richards': 92}]
# l4 = [ { j : k } for j, k in zip(l2, l3) ]

# res = [  { i : n } for i, n in zip(l1, l4)   ]

# print( res )


''' ---------- '''

# # Page's approach

# res = [ {i:{j:k}} for i, j, k in zip(l1, l2, l3) ]  #Truly fucking elegant

# print(res)





'''
45. Write a Python program to verify that all values in a dictionary are the same.

    Original Dictionary:

    {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

    Check all are 12 in the dictionary.
    True
    
    Check all are 10 in the dictionary.
    False
    
'''

# d =  {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

# p = 10

# print( all ( [ x == p for x in d.values() ] ) )





'''
46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.

    Original list:
    [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

    Grouping a sequence of key-value pairs into a dictionary of lists:
    {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
    
'''

# base = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]


''' ---------- '''

# # My Approach

# res = dict()

# for k,v in base:

#     if k in res.keys():        

#         res[k].append(v)

#     else:  

#         res[k] = list()

#         res[k].append(v)

# print(res)


''' ---------- '''


# # Page's approach

# res = dict()

# for k, v in base:

#     res.setdefault(k,[]).append(v) # More efficient

# print(res)





'''
47. Write a Python program to split a given dictionary of lists into lists of dictionaries. 

    Original dictionary of lists:
    {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

    Split said dictionary of lists into list of dictionaries:
    [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
        
'''


# d = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}


''' ------------ '''

# # My looping solution

# keys = list(d.keys())

# values = list(zip(*d.values()))

# res = list()

# for i, j in values:

#     dic1 = dict()

#     dic1[keys[0]], dic1[keys[1]] = i, j

#     res.append(dic1)

# print(res)

' --- '

# # My Listcomp solution

# keys = list(d.keys())

# res = [ {keys[0] : v[0], keys[1]: v[1]} for v in list(zip(*d.values()))  ] 

# print(res)


''' ------------ '''

# # Page's Solution

# keys = d.keys()

# values = zip(*d.values())

# res = [ dict( zip(keys, v) ) for v in values ]  # More readable

# print(res)





'''
49. Write a Python program to convert string values of a given dictionary into integer/float datatypes.

    Original list:
    [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

    String values of a given dictionary, into integer types:
    [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]


    Original list:
    [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
    
    String values of a given dictionary, into float types:
    [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
        
'''

# l =  [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]


''' ----------- '''

# # My Solution

# res = [ dict( zip( x.keys(), map( float, x.values() ) ) ) for x in l  ]

# print(res)


''' ----------- '''

# # Page's Solution

# res = [ { k : int(v) for k,v in dic.items() } for dic in l  ]   # it was just different

# print(res)





'''
50. A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.

    Original Dictionary:
    {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

    Clear the list values in the said dictionary:
    {'C1': [], 'C2': [], 'C3': []}
        
'''

# d = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

''' ----------- '''

# A quick solution of mine

# res = { k : [] for k, v in d.items() }  # Easiest way out

# print(res)


''' ----------- '''

# # Page's Solution

# for key in d:   d[key].clear()

# print(d)





'''
51. A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.

    Original Dictionary:
    {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

    Update the list values of the said dictionary:
    {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
        
'''

# d = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}


''' ------------ '''

# # My Solution

# updated_values = [ [89, 90, 91], [90, 92, 87], [90, 87, 93] ]

# # res = dict( zip( d.keys(), updated_values ) )   #Easiest way out

# res = {k: v for k, v in zip( d.keys(), updated_values ) }

# print(res)


''' ------------ '''

# # #Page's solution

# d['Math'] = [ x+1 for x in d['Math'] ]  # Didn't ocurred to me that a comprehension could be done within a Dict value. Nice!

# d['Physics'] = [ x-2 for x in d['Physics'] ]

# print(d)





'''
52. Write a Python program to extract a list of values from a given list of dictionaries.

    Original Dictionary:
    [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

    Extract a list of values from said list of dictionaries where subject = Science
    [92, 94, 88]

    Original Dictionary:
    [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

    Extract a list of values from said list of dictionaries where subject = Math
    [90, 89, 92]
        
'''

# d = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

# subject = 'Science'

# res = [ v[subject] for v in d ]

# print(res)





'''
53. Write a Python program to find the length of a dictionary of values.

    Original Dictionary:
    {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

    Length of dictionary values:
    {'red': 3, 'green': 5, 'black': 5, 'white': 5}

    Original Dictionary:
    {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

    Length of dictionary values:
    {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}
    
'''

# d = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

# res = { v: len(v) for v in d.values() }

# print(res)





'''
54. Write a Python program to get the depth of a dictionary.

    Expected Output: 4
    
'''

# d = {'a':1, 'b': {'c': {'d': {}}}}


# # This is not a solution of mine, it came from the page. Apparently it involves recursions which I am not familiar with at the moment


# def dict_depth(d):

#     if isinstance(d, dict):

#         return 1 + ( max( map ( dict_depth, d.values() ) ) if d else 0 )
    
#     return 0

# print(dict_depth(d))





'''
55. Write a Python program to access dictionary key's element by index. 

    Expected Output:
    physics
    math
    chemistry
    
    
'''

# d = {'physics': 80, 'math': 90, 'chemistry': 86}

# i = 2

# res = list(d)[i]

# print(res)





'''
56. Write a Python program to convert a dictionary into a list of lists.

    Original Dictionary:
    {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

    Convert the said dictionary into a list of lists:
    [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

    Original Dictionary:
    {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

    Convert the said dictionary into a list of lists:
    [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
        
'''

# d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

# res = [ list(x) for x in d.items()]

# print(res)





'''
57. Write a Python program to filter even numbers from a dictionary of values.

    Original Dictionary:
    {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

    Filter even numbers from said dictionary values:
    {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

    Original Dictionary:
    {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

    Filter even numbers from said dictionary values:
    {'V': [], 'VI': [], 'VII': [2]}
        
'''

# d = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

# res = { k: [x for x in v if x%2 == 0] for k,v in d.items() }

# print(res)





'''
58. Write a Python program to get all combinations of key-value pairs in a given dictionary.

    Original Dictionary:
    {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

    Combinations of key-value pairs of the said dictionary:
    [{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]

    Original Dictionary:
    {'V': [1, 3, 5], 'VI': [1, 5]}

    Combinations of key-value pairs of the said dictionary:
    [{'V': [1, 3, 5], 'VI': [1, 5]}]
        
'''

# d = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

# # [('V', [1, 4, 6, 10]), ('VI', [1, 4, 12]), ('VII', [1, 3, 8])]
# l = list( d.items() )

# res = list()

# for i in range( len(l) - 1 ):

#     for j in range( i+1 , len(l)):

#         res.append( [l[i], l[j]] )


# res = list( map( dict, res ) )

# print (res)





'''
59. Write a Python program to find the specified number of maximum values in a given dictionary. 

    Original Dictionary:
    {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

    1 maximum value(s) in the said dictionary:
    ['f']

    2 maximum value(s) in the said dictionary:
    ['f', 'i']

    5 maximum value(s) in the said dictionary:
    ['f', 'i', 'g', 'd', 'c']
        
'''


# d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}


''' ---------- '''

# # My Solution

# n = 5

# res = [ x for x in sorted(d.items(), key = lambda x: x[1], reverse = True)]

# print( [ x[0] for x in res[:n] ] ) 


''' ---------- '''

# # Page's solution

# n = 5

# res = sorted(d, key = d.get, reverse = True)[:n]

# print(res)





'''
60. Write a Python program to find the shortest list of values for the keys in a given dictionary. 

    Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 

    Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']
'''

# d = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 

# res = [ x[0] for x in d.items() if len(x[1]) == min( [ len(y) for y in d.values() ] ) ]

# print(res)





'''
61. Write a Python program to count the frequency of a dictionary.

    Original Dictionary:
    {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

    Count the frequency of the said dictionary:
    Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})
'''

# d = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

# res = { v: list(d.values()).count(v) for v in list(d.values()) }

# print(res)





'''
62. Write a Python program to extract values from a given dictionary and create a list of lists from those values. 

    Original Dictionary:
    [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
    
    Extract values from the said dictionarie and create a list of lists using those values:
    
    [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
    [[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
    [['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]

'''

# d = [
#     {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#     {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, 
#     {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
#     {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
#     {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
#     ]


''' ---------- '''

# # My Solution

# items = [ list(x.values()) for x in d ]

# print( [ x for x in items ], end='\n' )

# print( [ x[:2] for x in items ], end='\n' )

# print( [ x[1:] for x in items ], end='\n' )


''' ---------- '''

# # Page's Solution

# def test(dictt, keys):
    
#     return [ list(d[k] for k in keys) for d in dictt ]


# print(test(d, ('student_id', 'name', 'class')))

# print(test(d, ('student_id', 'name')))

# print(test(d, ('name', 'class')))

# print(res)





'''
67. Write a Python program to invert a given dictionary with non-unique hashable values. 

    Input: students = {'Ora Mckinney': 8,'Theodore Hollandl': 7,'Mae Fleming': 7,'Mathew Gilbert': 8,'Ivan Little': 7}

    Sample Output: {8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}

'''

# d = {'Ora Mckinney': 8, 'Theodore Hollandl': 7, 'Mae Fleming': 7, 'Mathew Gilbert': 8,'Ivan Little': 7}

# groups =  { v1 : [k for k,v in d.items() if v == v1] for v1 in set(d.values()) }

# print(groups)





'''
68. Write a Python program to combine two or more dictionaries, creating a list of values for each key.

    Sample Output:

    Original dictionaries:
    {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
    {'x': 300, 'y': 'Red', 'z': 600}

    Combined dictionaries, creating a list of values for each key:
    {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}

'''

# d1, d2 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}, {'x': 300, 'y': 'Red', 'z': 600}

# keys = set( [ k for elem in ( [x for x in d1.keys()], [x for x in d2.keys()] ) for k in elem ] )

# res = dict()

# for k in keys:

#     if k in d1 and k in d2: 

#         res[k] = [ d1[k], d2[k] ]

#     else: res[k] = [d1[k]]

# print(res)





'''
69. Write a Python program to group the elements of a given list based on the given function.

    Sample Output:

    Original list & function:
    [7, 23, 3.2, 3.3, 8.4] Function name: floor:

    Group the elements of the said list based on the given function:
    {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}


    Original list & function:
    ['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:

    Group the elements of the said list based on the given function:
    {3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}

'''

# import math

# d = [7, 23, 3.2, 3.3, 8.4]

# d2 = ['Red', 'Green', 'Black', 'White', 'Pink']

# func = len


# ''' ----------- '''

# # My solution

# keys = sorted( [x for x in set( map( func, d2 ) ) ] )

# res = { k : [] for k in keys }

# for v in d2:

#     if func(v) in keys:   res[ func(v) ].append(v) 


# print(res)





'''
70. Write a Python program to map the values of a given list to a dictionary using a function, 
where the key-value pairs consist of the original value as the key and the result of the function as the value. 

    Sample Output:
    {1: 1, 2: 4, 3: 9, 4: 16}

'''

# keys = [1,2,3,4]

# func = lambda x: x*x

# values = [ x for x in map(func, keys) ]

# res = dict(zip(keys, values))

# print(res)





'''
75. Write a Python program to find all keys in a dictionary that have the given value. 

    Sample Output:

    Original dictionary elements:
    {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

    Find all keys in the said dictionary that have the specified value:
    ['Roxanne', 'Betty']

'''

# d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

# res = [ k for k,v in d.items() if v == 20 ]

# print(res)





'''
80. Write a Python program to find the key of the maximum value in a dictionary. 

    Sample Output:

    Original dictionary elements:
    {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

    Finds the key of the maximum and minimum value of the said dictionary:
    ('Roxanne', 'Theodore')

'''

# d = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}


''' ----------- '''

# # My solution

# res = [k for k,v in d.items() if v == max(d.values())]+[k for k,v in d.items() if v == min(d.values())]

# print(res)


''' ----------- '''

# # Page's solution

# res = ( max( d, key = d.get ), min( d, key = d.get ) )

# print(res)






















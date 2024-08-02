'''
Itertools tutorial
'''

import itertools


'counter'

# counter = itertools.count()

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(counter)
# print(type(counter))


# data = [125, 478, 856, 936]

# daily_data = list(zip(itertools.count(),data))

# daily_data = list(zip(itertools.count(start=5, step=5),data))

# print(daily_data)



'zip_longest'

# data = [125, 478, 856, 936]

# daily_data = list(itertools.zip_longest(range(6),data))

# print(daily_data)



'cycle'

# data = ['a', 'b', 'c']

# cycle_data = itertools.cycle(data)

# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))
# print(next(cycle_data))


# switch = itertools.cycle(['On', 'Off'])

# print(next(switch))
# print(next(switch))
# print(next(switch))



'repeat'

# repeated_valued = itertools.repeat(2)

# print(next(repeated_valued))
# print(next(repeated_valued))
# print(next(repeated_valued))

# repeated_valued = itertools.repeat(2, times = 2)

# print(next(repeated_valued))
# print(next(repeated_valued))
# print(next(repeated_valued))


# squares = list( map(pow, range(10), itertools.repeat(2)))

# print(squares)


# matches = list(range(5))

# matched = list( zip(matches, itertools.repeat('x')) )

# print(matched)



'starmap'

# squares = list( itertools.starmap( pow, [(x, 2) for x in range(5)] ) )

# print(squares)



'combinations'

# combinations = list( itertools.combinations('abcd', 2) )

# print(combinations)



'combinations with replacement'

# combinations = list( itertools.combinations_with_replacement('abcd', 2) )

# print(combinations)



'permutations'

# permutations = list( itertools.permutations('abcd', 4) )

# print(len(permutations))



'product'

# numbers = [1,2,3,4]

# product = itertools.product(numbers, repeat = 4 )

# print(len(list(product)))



'chain'

# li1 = ['a','b','c']

# li2 = (1,2,3,4)

# li3 = {None, True, False}

# comb = itertools.chain(li1, li2, li3)

# print( [x for x in comb] )



'islice'

# itslice = itertools.islice(range(10), 2, 8, 2)

# print( [x for x in itslice] )



'Compress'

# data = ['a','b','c','e']

# selectors = [1,0,1,1]

# compress = itertools.compress(data, selectors)

# print([x for x in compress])



'filtersalse'

# def fn(num):

#     if num%2 == 0: 
#         return True
    
#     else:
#         return False
    

# data = [x for x in range(21)]

# filterfalse = itertools.filterfalse(fn, data)

# print([x for x in filterfalse])



# data2 = [x for x in 'Ax.1e3"$sRT?']

# filterfalse = itertools.filterfalse( str.isnumeric, data2 )

# print([x for x in filterfalse])



'dropwhile'

# data = [-4, -3, 17, 9, 14, 12, -7, -4, 16, 0, 19]

# iterator = itertools.dropwhile(lambda x: x < 0, data)

# print(list(iterator))



'takewhile'

# data = [-4, -3, 17, 9, 14, 12, -7, -4, 16, 0, 19]

# iterator = itertools.takewhile(lambda x: x < 0, data)

# print(list(iterator))



'accumulate'

# data = [1, 2, 3, 4, 5, 6]

# result = itertools.accumulate(data)

# print([x for x in result])



# cashflows = [1000, -90, -90, -90, -90]

# amortization = itertools.accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)

# print([f'{x:.2f}' for x in amortization])



'groupby'

# people = [
    
#     {
#         'name': 'John Doe',
#         'city': 'Gotham',
#         'state': 'NY'
#     },
#     {
#         'name': 'Jane Doe',
#         'city': 'Kings Landing',
#         'state': 'NY'
#     },
#     {
#         'name': 'Corey Schafer',
#         'city': 'Boulder',
#         'state': 'CO'
#     },
#     {
#         'name': 'Al Einstein',
#         'city': 'Denver',
#         'state': 'CO'
#     },
#     {
#         'name': 'John Henry',
#         'city': 'Hinton',
#         'state': 'WV'
#     },
#     {
#         'name': 'Randy Moss',
#         'city': 'Rand',
#         'state': 'WV'
#     },
#     {
#         'name': 'Nicole K',
#         'city': 'Asheville',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jim Doe',
#         'city': 'Charlotte',
#         'state': 'NC'
#     },
#     {
#         'name': 'Jane Taylor',
#         'city': 'Faketown',
#         'state': 'NC'
#     }
# ]


# sorted_people = [x for x in sorted(people, key = lambda x: x['state'], reverse = False)]

# grouped_people = itertools.groupby(sorted_people, key = lambda x: x['state'] )

# for k, g in grouped_people:

#     print(k, list(g))
  

   

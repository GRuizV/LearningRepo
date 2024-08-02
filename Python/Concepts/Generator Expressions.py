
'Recap of Generator Functions'

# def my_range(start, end):

#     current = start

#     while current < end:

#         yield current

#         current += 1
	

# gen_func = my_range(0,2)

# print(next(gen_func))   # 0
# print(next(gen_func))   # 1
# print(next(gen_func))   # StopIteration Expection




'Now, Generator Expressions'

# n = 2
# gen_exp = (x for x in range(n))
	

# print(next(gen_exp))   # 0
# print(next(gen_exp))   # 0
# # print(next(gen_exp))   # StopIteration Expection





'How to know where is the iteration at any moment?, with a wrapper'


# def gen_counter(generator):

#     count = 0

#     for value in generator:

#         count += 1

#         yield value, count


# def generator():

#     yield 'D'
#     yield 'Q'
#     yield 'U'


# gen_func = gen_counter(generator())

# print(next(gen_func))   # ('D', 1)
# print(next(gen_func))   # ('Q', 2)
# print(next(gen_func))   # ('U', 3)







import array as arr
from timeit import default_timer as timer


# Most common _typecodes are: 'i' for integers, 'f' for float, 'c' characters, 's' strings.
new_arr = arr.array('i',[x for x in range(100)])



'Printing an Array'
# print(new_arr)  # array('i', [1, 2, 3, 4, 5, 6])



'Accesing items in an Array'
# print(new_arr[1], new_arr[-1], new_arr[0])  # 2 6 1

# print(new_arr[7])  # Exception has occurred: IndexError - array index out of range



'Inserting items in an Array'
# new_arr.insert(0,10)

# print(new_arr)  # array('i', [10, 1, 2, 3, 4, 5, 6])

# new_arr.insert(7,11)

# print(new_arr)  # array('i', [10, 1, 2, 3, 4, 5, 6, 11])

# # new_arr.insert('x',12)  # Exception has occurred: TypeError - 'str' object cannot be interpreted as an integer

# new_arr.insert(15,40)   # it still understands an index way far from the end of the array as its last index

# print(new_arr)  # array('i', [10, 1, 2, 3, 4, 5, 6, 11, 40])

# new_arr.insert(-20,100)   # same goes backwards

# print(new_arr)  # array('i', [100, 10, 1, 2, 3, 4, 5, 6, 11, 40])



'Removing items in an Array'
# new_arr.remove(1)

# print(new_arr) # array('i', [2, 3, 4, 5, 6])

# # new_arr.remove('x') # Exception has occurred: ValueError - array.remove(x): x not in array

# del new_arr[-1]

# print(new_arr)  # array('i', [2, 3, 4, 5])



'Updating items in an Array'
# new_arr[0] = 25

# print(new_arr)  # array('i', [25, 2, 3, 4, 5, 6])

# new_arr[-1] = 'x'   # Exception has occurred: TypeError - 'str' object cannot be interpreted as an integer



'Array searching'

# s = timer()

# item = None

# for i in new_arr:

#     if i == new_arr[-1]:

#         item = i

# e = timer()

# print(f' Item: {item}', f' time elapsed: {e-s:.7f}s')
























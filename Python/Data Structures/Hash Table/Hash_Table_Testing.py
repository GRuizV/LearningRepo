import sys
from Hash_Table_Implementation_RP import HashTable


'Hand-made hash function'

def hash_function(text):

    return sum( index * ord(char) for index, char in enumerate(text, start=1))


# print(hash_function("Tiny"))
# # 1108

# print(hash_function("This has a somewhat medium length."))
# # 56294

# print(hash_function("This is very long and slow!" * 1_000))
# # 33305415500


# print(f'{sys.maxsize:_}') # Represents the highest value of integers supported natively in Python.







'Hash Table implementation testing'

# Creating a dummy HT
hash_table = HashTable(capacity=10)

#Adding key-value pairs
hash_table['Hello'] = 'Hola'
hash_table[10] = 35
hash_table[None] = True

# #Checking the actual HT values
# print(hash_table.values)

# #Checking that the values actually exist in the HT
# print(hash_table['Hello'])
# print(hash_table[10])
# print(hash_table[None])

# #Checking a missing key in the HT
# print(hash_table['x'])

a = [(1,2), ('a','b'), ('c', 'd')]

d = {k:v for k,v in a}

print(d.items())




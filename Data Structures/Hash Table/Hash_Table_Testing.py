import sys


'Hand-made hash function'


def hash_function(text):

    return sum( index * ord(char) for index, char in enumerate(text, start=1))


# print(hash_function("Tiny"))
# # 1108

# print(hash_function("This has a somewhat medium length."))
# # 56294

# print(hash_function("This is very long and slow!" * 1_000))
# # 33305415500


print(f'{sys.maxsize:_}') # Represents the highest value of integers supported natively in Python.






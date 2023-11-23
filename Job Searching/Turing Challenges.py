
'Problem #2'
# def solutions(s):

#     s = s.split('-')

#     animals = [x for x in s if x != '']

#     return len(animals[-1])

# print( solutions("Elephant-Tiger-Lion-") )


# s = "-Elephant-Tiger-Lion-"

# print(s.split('-'))



'Problem #1'

'''
    The problem statement is how many ways are to reach to the 
    top of a trail of rocks if you can jump only 1 or 2 rocks at
    a time.

    According to chatGPT this is a fibonacci pattern, and I FUCKING HATE IT.

'''

def fibonacci(n):

    result = [0,1]

    for i in range(n):
        result.append(sum(result[-2:]))

    return result


print(fibonacci(7))
















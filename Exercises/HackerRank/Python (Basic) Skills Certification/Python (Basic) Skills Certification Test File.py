'2. String Transformation'

# Input

# Case 1
# sentence = 'coOL dog' # Expected Output: cOOl dOg

# Case 2
# sentence = 'a Blue MOON' # Expected Output: a BLUe MOOn

# Case 3
# sentence = 'ab cB GG' # Expected Output: aB cb GG

# Case 4
# sentence = 'x y z' # Expected Output: x y z

# Note
# Letters order: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


# My approach

# def tranformSentence(sentence):

#     strings = sentence.split()
#     result = []

#     for string in strings:

#         for i in range(1, len(string)):

#             x = string[i].casefold()
#             y = string[i-1].casefold()

#             if x != y :

#                 if x > y:
                    
#                     x = x.upper()
#                     string = string[:i] + x + string[i+1:]
                
#                 else:

#                     x = x.lower()
#                     string = string[:i] + x + string[i+1:]
        
#         result.append(string)

    
#     result = ' '.join(result)

#     return result


# print(tranformSentence(sentence))
                
'Notes: It works!'




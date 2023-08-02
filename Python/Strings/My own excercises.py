
''' 

    I started to do this with the purpose of learning but 
    while going thru some tutorial I found that the method ".title()"
    does exactly what I wanted.

'''



'''Here is the example with the .title() method'''

# sentence = 'hi there! my name is aegon targaryen and i came to roast your ass'

# print(sentence.title())




'''

Own Excercise, try to find something and returned but capitalized manually

    I want to create a way to receive something and return it but witch the initial letter capitalized

'''

# sentence = 'hi there! my name is aegon targaryen and i came to roast your ass'

# new_sentence = sentence.split()

# final_sentence = []

# for i in new_sentence:

#     final_sentence.append(i.capitalize())

# final_sentence = ' '.join(final_sentence)

# print(final_sentence)





''' Same as the last, but with a function creation'''

# sentence = 'hi there! my name is aegon targaryen and i came to roast your ass'

# print(f'The initial sentence is: {sentence}')

# def capitalizer (str):

#     new_str = str.split()

#     final_str = []

#     for i in new_str:

#         final_str.append(i.capitalize())

#     final_str = ' '.join(final_str)

#     return final_str

# sentence = capitalizer(sentence)

# print (f'The final sentence is: {sentence}')




''' Now, let's try to do the same but with the last letter '''

# sentence = 'hi there! my name is aegon targaryen and i came to roast your ass'

# sentence = sentence[::-1]

# new_sentence = sentence.split()

# final_sentence = []

# for i in new_sentence:

#     final_sentence.append(i.capitalize())

# final_sentence = ' '.join(final_sentence)

# final_sentence = final_sentence[::-1]

# print (final_sentence)

# Note: it worked but a thing arose, as the second word contains a non-letter character, it wouldn't capitalize it


''' format_map() '''

# s = 'Hey, there! my name is {name}'

# d = {'name' : 'Gerardo'}

# print(s.format_map(d))

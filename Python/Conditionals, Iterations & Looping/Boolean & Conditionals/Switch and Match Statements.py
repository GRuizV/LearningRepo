
"""
Swtich case implementation in python by defining a function

"""

# dic = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

# def switch(value):
#     return dic.get(value, "Not Found")

# print(switch(int(input('input number:'))))



"""
The Match Statement

"""

# # Base form
# def size_match(size):

#     match size:

#         case 32:
#             print("Slim")

#         case 36:
#             print('Medium')

#         case 42:
#             print('Thick')


# size_match(32)


'''------------'''


# # grouped patterns
# def size_match(size):

#     match size:

#         case 32 | 34:
#             print("Slim")

#         case 36 | 38:
#             print('Medium')

#         case 40 | 42:
#             print('Thick')


# size_match(38)


'''------------'''


# # Bind varibales
# def point_match(point):

#     match point:
        
#         case (0, 0):
#             print("In origin")

#         case (int(), 0):
#             print('In x-axis')

#         case (0, value):
#             print('In y-axis')

#         case _:
#             print(f'Match not found')


# point_match((0,5))
# point_match((8,0))
# point_match(('y','y'))


'''------------'''


# # With conditionals
# def grade_match(grade):

#     match grade:
        
#         case grade if grade >= 90:
#             print("A")
        
#         case grade if grade >= 80:
#             print("B")
        
#         case grade if grade >= 70:
#             print("C")
        
#         case grade if grade >= 60:
#             print("D")
        
#         case _:
#             print("F")



# grade_match(95)
# grade_match(72)


'''------------'''


# # With membership
# def poketype_match(poketype):

#     match poketype:
        
#         case poketype if poketype in ['Grass', 'Ice', 'Bug', 'Steel']:
#             print("Vulnerable to Fire type")

#         case poketype if poketype in ['Fire', 'Ground', 'Rock']:
#             print("Vulnerable to Water type")

#         case poketype:
#             print(f'{poketype} type not updated yet')
        


# poketype_match('Ice')

# poketype_match('Ghost')
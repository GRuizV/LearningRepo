
person = {'name': 'Jenn', 'age': 23}


# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'


# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)

# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)



'''fString version'''
# sentence = f'My name is {person["name"]} and I am {person["age"]} years old.'




'''This would be made if comming from an object's attribute'''
# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Jack', '33')

# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)



'''FStringed'''
# sentence = f'My name is {p1.name} and I am {p1.age} years old.'

# Another way to do it
# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn',age=23)




'''Unpacking dictionaries'''

# sentence = 'My name is {name} and I am {age} years old.'.format(**person)




''' .format_map() string method'''


# # With only one placeholder:

# s = 'Hey, there! my name is {name}'

# d = {'name' : 'Gerardo'}

# print(s.format_map(d))



# # With two placeholders:

# s = 'Coordinates are: x: {x}; y: {y} '

# d = {'x' : 14, 'y' : 3 }

# print(s.format_map(d))


# # Compared to the .format(**dict):

# s = 'Coordinates are: x: {x}; y: {y} '

# d = {'x' : 14, 'y' : 3 }

# print(s.format(**d))



# # With Class inherited dictionary:

# class Foo (dict):
#     def __missing__(self, key):
#         return 'Not Found!'

# print('( x: {x} ; y: {y} )'.format_map(Foo({'x': 3}))) 


# # Compared to the .format(**dict):

# class Foo (dict):
#     def __missing__(self, key):
#         return 'Not Found!'

# print('( x: {x} ; y: {y} )'.format(**Foo({'x': 3, 'y':7}))) 



s = 'Milk\nChicken\nBread\nButter'

print(s)
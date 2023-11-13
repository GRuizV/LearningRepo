
'Classes'

# # Class example definition
# class Employee:

#     def __init__(self, name, age):

#         self.name = name
#         self.age = age




'Class practical case'

# #   Class creation
# class Dog:

#     species = 'Canis familiaris' # Class Variable
    
#     def __init__(self, name, age):  # Initializator method
        
#         self.name = name    # Instance Variables
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"





#     # Instance methods

#     def description(self):
#         return f"{self.name} is {self.age} years old"
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"







# # Class instantiation
# juno = Dog('Juno', 0)


# Class & Instance Testing
# print(juno.name) # Juno
# print(juno.age) # 0

# print(juno.species) # Canis familiaris


'    Note: Custom objects are mutable!'

# juno.species = 'Felis silvestris'

# print(juno.species) # Felis silvestris


# print(juno.description())   # Juno is 0 years old
# print(juno.speak('Woof Woof'))  # Juno says Woof Woof
# print(juno.speak('Bow Wow'))    # Juno says Bow Wow


# Instance representation
# print(juno) # <__main__.Dog object at 0x0000020E13637170> 

'    after implementing the __str__() method'

# print(juno) # Juno is 0 years old




'Inheritance'

# class Parent:
#     hair_color = "brown"


# class Child(Parent):
#     pass


# kyle = Child()
# print(kyle.hair_color)  # brown



# # Overriding

# class Child(Parent):
#     hair_color = "purple"

# jake = Child()

# print(jake.hair_color)  # purple




# # Extending

# class Parent:

#     speaks = ["English"]



# class Child(Parent):

#     def __init__(self):

#         super().__init__() 

#         self.speaks.append("German")




# jake = Child()

# print(jake.speaks)  # ['English', 'German']




'   Dog Park Example'

class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
         return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):

    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):

    def speak(self, sound="Woof"):
        return super().speak(sound)
    

class Bulldog(Dog):

    def __init_subclass__(cls):
        return super().__init_subclass__()
    

class GoldenRetriever(Dog):

    def speak(self, sound = "Bark"):
        return super().speak(sound)
  
   


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

bosco = GoldenRetriever("Bosco", 8)


print(miles.speak())    # Miles says Arf

print()

print(buddy.speak())    # Jack barks: Woof

print()

print(jack.speak('Arrf'))     # Jack barks: Arrf
print(jim.speak('Woof'))      # Jim barks: Woof
print()

print(bosco.speak())     # Bosco barks: Bark

# print(isinstance(miles, Dog))

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
#         self.__condition = 'Healthy'    #Private Variable (Attribute)
#         self._owner = None  # Protected Variable (Attribute)
    
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"




#     # Faux Class method
#     def faux_bark():
#         return print(f'Dog just barked!!')
    
#     # Actual class method
#     @classmethod
#     def bark(cls):
#         return print(f'Dog just barked!!')

#     @classmethod
#     def species_change(cls, new_species):
#         cls.species = new_species




#     # Pythonic Getters, Setters & Deleters

#     @property   # Getter
#     def condition(self):
#         return self.__condition
    
#     @condition.setter   # Setter
#     def condition(self, condition):
#         self.__condition = condition

#     @condition.deleter
#     def condition(self):
#         del self.__condition

#     @property   # Getter
#     def owner(self):
#         return self._owner
    
#     @owner.setter   # Setter
#     def owner(self, owner):
#         self._owner = owner

#     @owner.deleter
#     def owner(self):
#         del self._owner




#     # Instance methods

#     def description(self):
#         return f"{self.name} is {self.age} years old"
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"





# # Class instantiation
# juno = Dog('Juno', 0)


# # # Class & Instance Testing
# # print(juno.name) # Juno
# # print(juno.age) # 0

# # print(juno.species) # Canis familiaris

# # # Class method doesn't need to be instantiated but it could only run on the class
# # Dog.faux_bark()   # Dog just barked!!


# '''
# But it isn't correctly stated is it's supposed to be class method, because if it does,
# it should have the @classmethod decorator and recieve the 'cls' first argument instead of 'self'

#     The more technical specification is that while a function is defined as the bark method without
#     the decorator it acts like a class method but it doen't have access to modify the class attributes,
#     so in essence is just a function that can be called directly from the class but that's it.
# '''

# # # Corrected Class method.
# # Dog.bark()  # Dog just barked!!


# # # Class methods in action
# # print(f"{juno.name} species is: {juno.species}", end='\n\n') # Canis familiaris

# # '    Note: Custom objects are mutable!'
# # juno.species = 'Felis Silvetris'

# # print(f"{juno.name} species is now: {juno.species}", end='\n\n') # Felis Silvestris

# # print(f"All Dogs (Dog Class) are still: {Dog.species}")  # Canis familiaris, remain unchanged

# # rex = Dog('Rex', 5)

# # print()
# # print(f"{rex.name} species is: {rex.species}", end='\n\n') # Canis familiaris

# # Dog.species_change('Turdus migratorius')
# # print(f"Now all Dogs (Dog Class) will be 'Turdus migratorius' from here on...", end='\n\n')

# # print(f"{rex.name} species is now: {rex.species}", end='\n\n') # Canis familiaris


# '   An Example of the use of @Classmethods'
# # The task is to implement an instance counter in the definition of a Class


# class Item:

#     instances = int()

#     def __init__(self):

#         Item.instances += 1
#         print(f'Item #{self.instances} created')



#     @classmethod
#     def instantiator(cls, count):

#         for _ in range(count):
#             Item()


# item1 = Item()

# print(f"There currently ({Item.instances}) instances in the class")

# Item.instantiator(5)

# print(f"There currently ({Item.instances}) instances in the class")




# # # Instance methods testing
# # print(juno.description())   # Juno is 0 years old
# # print(juno.speak('Woof Woof'))  # Juno says Woof Woof
# # print(juno.speak('Bow Wow'))    # Juno says Bow Wow


# # # Instance representation
# # print(juno) # <__main__.Dog object at 0x0000020E13637170> 

# # '    after implementing the __str__() method'

# # print(juno) # Juno is 0 years old


# # # Getters and Setters

# # print(juno.name)    # Juno

# # print(juno.__condition) # Private attributes are directly inaccessibles
# print(juno.condition) # Healty, The getter works
# juno.condition = 'Sick' # Setter
# print(juno.condition) # Sick, The getter still works
# del juno.condition  # Deletter implemented
# print(juno.condition) # AttributeError, Means it worked


# # print(juno._owner)  # protected attributes are directly accessibles, but aren't supposed to be accessed directly
# print(juno.owner) # None, The getter works
# juno.owner = 'Juan' # setter
# print(juno.owner) # Juan, The getter still works
# del juno.owner # Deletter implemented
# print(juno.owner) # AttributeError, Means it worked






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




# '   Dog Park Example'

# class Dog:

#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#          return f"{self.name} barks: {sound}"


# class JackRussellTerrier(Dog):

#     def speak(self, sound="Arf"):
#         return f"{self.name} says {sound}"


# class Dachshund(Dog):

#     def speak(self, sound="Woof"):
#         return super().speak(sound)
    

# class Bulldog(Dog):

#     def __init_subclass__(cls):
#         return super().__init_subclass__()
    

# class GoldenRetriever(Dog):

#     def speak(self, sound = "Bark"):
#         return super().speak(sound)
  
   


# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)

# bosco = GoldenRetriever("Bosco", 8)


# print(miles.speak())    # Miles says Arf

# print()

# print(buddy.speak())    # Jack barks: Woof

# print()

# print(jack.speak('Arrf'))     # Jack barks: Arrf
# print(jim.speak('Woof'))      # Jim barks: Woof
# print()

# print(bosco.speak())     # Bosco barks: Bark

# print(isinstance(miles, Dog))



# '   Another example of In heritance: With the __init__'

# class Employee:

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary


# class SoftwareEngineer(Employee):

#     def __init__(self, name, age, salary, level):
#         super().__init__(name, age, salary)
#         self.level = level

#     def __str__(self):
#         return f"Employee name: '{self.name}'\nEmployee age:'{self.age}'\nSalary: ${self.salary:,}\nLevel: {self.level}"


# jerry = SoftwareEngineer('Jerry', 30, 7000, 'Junior')

# print(jerry)

# # Printout
# # Employee name: 'Jerry'
# # Employee age:'30'
# # Salary: $7,000
# # Level: Junior


# '   This is why the super() function is important'

# class Parent:
#     def method(self):
#         print("Parent method")


# class Child(Parent):
#     def method(self):
#         print("Child method")
#         super().method()  # Calls the method from the Parent class


# Child().method()    #This will print "Child method\nParent method"






'Polymorphism'

# #This is inheritance, NOT polymorphism
# print('*Inheritance*\n')
# class Animal:

#     def speak(self):
#         return print('Generic animal sound')


# class Dog(Animal):

#     def bark(self):
#         return print('Woof!')


# class Cat(Animal):

#     def meow(self):
#         return print('Meow!')


# doggo = Dog() 
# catto = Cat()


# doggo.speak() # Generic animal sound
# catto.speak() # Generic animal sound

# print()

# doggo.bark() # Woof!
# catto.meow() # Meow!


# #This is polymorphism (Runtime polymorphism)
# print('\n*Polimorphism (Runtime)*\n')
# class Animal:

#     def intro(self):
#         return print('Hi, Im an animal')
    
#     def speak(self):
#         return print('Generic animal sound')


# class Dog(Animal):

#     def speak(self):
#         return print('Woof!')


# class Cat(Animal):

#     def speak(self):
#         return print('Meow!')


# doggo = Dog()
# catto = Cat()

# doggo.intro() # Hi, Im an animal
# doggo.speak() # Woof!
# print()

# catto.intro() # Hi, Im an animal
# catto.speak() # Meow!






'Encapsulation'

# class Car:

#     def __init__(self, make, model, year):

#         self.__make = make  # Encapsulated attribute
#         self.__model = model  # Encapsulated attribute
#         self.__year = year  # Encapsulated attribute
#         self.__odometer_reading = 0  # Encapsulated attribute


#     # Getter methods
#     def get_make(self):
#         return self.__make

#     def get_model(self):
#         return self.__model

#     def get_year(self):
#         return self.__year

#     def get_odometer_reading(self):
#         return self.__odometer_reading


#     # Setter method for odometer reading with validation
#     def update_odometer(self, mileage):

#         if mileage >= self.__odometer_reading:
#             self.__odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")


#     # Method to increment odometer reading
#     def increment_odometer(self, miles):

#         if miles >= 0:
#             self.__odometer_reading += miles
#         else:
#             print("Please provide a positive value for mileage.")





# # Creating an instance of the Car class
# my_car = Car("Toyota", "Corolla", 2022)

# # Accessing attributes using getter methods
# print(f"Car: {my_car.get_year()} {my_car.get_make()} {my_car.get_model()}") # Car: 2022 Toyota Corolla
# print(f"Odometer reading: {my_car.get_odometer_reading()} miles") # Odometer reading: 0 miles


# '''
# Warning!

#     # Trying to directly access and modify the encapsulated attribute (not recommended)
#     # This won't work due to encapsulation (private attribute)
#     # print(my_car.__odometer_reading)  # This would cause an AttributeError'''

# # print(f"Car: {my_car.__year} {my_car.__make} {my_car.__model}") #  AttributeError: 'Car' object has no attribute '__year' [...]
# # print(f"Odometer reading: {my_car.__odometer_reading} miles")   #  AttributeError: 'Car' object has no attribute '__odometer_reading'

# '   There is actually a way around, in python there is nothing truly private...'
# # print(f"Car: {my_car._Car__year} {my_car._Car__make} {my_car._Car__model}") #  AttributeError: 'Car' object has no attribute '__year' [...]
# # print(f"Odometer reading: {my_car._Car__odometer_reading} miles")   #  AttributeError: 'Car' object has no attribute '__odometer_reading'




# # Modifying the odometer reading using the setter method
# my_car.update_odometer(1000)

# # Incrementing odometer reading
# my_car.increment_odometer(500)

# # Displaying updated odometer reading
# print(f"Updated odometer reading: {my_car.get_odometer_reading()} miles")   # Updated odometer reading: 1500 miles






'Abstraction'

# from abc import ABC, abstractmethod

# # Abstract Database class defining the blueprint for database interaction
# class Database(ABC):

#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def connect(self):
#         pass

#     @abstractmethod
#     def query(self, query):
#         pass

#     @abstractmethod
#     def update(self, query, data):
#         pass


# # Concrete class implementing Database for MySQL
# class MySQLDatabase(Database):

#     def connect(self):
#         print(f"Connecting to MySQL database: {self.name}")

#     def query(self, query):
#         print(f"Executing MySQL query: {query}")

#     def update(self, query, data):
#         print(f"Updating MySQL data: {query} with {data}")

# # Concrete class implementing Database for MongoDB
# class MongoDBDatabase(Database):
#     def connect(self):
#         print(f"Connecting to MongoDB database: {self.name}")

#     def query(self, query):
#         print(f"Executing MongoDB query: {query}")

#     def update(self, query, data):
#         print(f"Updating MongoDB data: {query} with {data}")



# # Using the abstract Database class without knowing the details
# # Instantiating objects of different database types
# mysql_db = MySQLDatabase("MySQL_DB")
# mongo_db = MongoDBDatabase("MongoDB_DB")

# # Performing database operations without knowing internal details
# mysql_db.connect()
# mysql_db.query("SELECT * FROM table")
# mysql_db.update("UPDATE table SET column = value", {"key": "value"})

# mongo_db.connect()
# mongo_db.query("db.collection.find()")
# mongo_db.update("db.collection.update()", {"key": "value"})



# '   the abc Module in Abstract Classes and Methods'

# from abc import ABC, abstractmethod

# class MyAbstractClass(ABC):

#     @abstractmethod
#     def my_abstract_method(self):
#         pass

#     @abstractmethod
#     def my_abstract_method2(self):
#         pass

# ' Attempting to create an instance of the abstract class'
# # my_object = MyAbstractClass()  # This line will raise an error

# class MyDerivedClass(MyAbstractClass):

#     def my_abstract_method(self):
#         pass
    
#     def my_abstract_method2(self):
#         pass

# my_derived_object = MyDerivedClass() # If either of the abs methods is not implemented, it'll in a TypeError














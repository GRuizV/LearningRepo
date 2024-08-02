from pympler import asizeof


'Using .__slots__ to lightweight classes'

# class Point1:

#     def __init__(self, x, y):

#         self.x = x
#         self.y = y


# point1 = Point1(4, 8)

# # print(point1.__dict__)  # .__dict__ is automatically created if .__slots__ is not defined

# print(asizeof.asizeof(point1))  # 504 bytes of memory being used

# point1.z = 5

# print(point1.z)


# '   Now, using __slots__'

# class Point2:

#     __slots__ = ("x", "y")  # Using mutables (like lists) here could be misleading

#     def __init__(self, x, y):

#         self.x = x
#         self.y = y


# point2 = Point2(4, 8)

# # print(point2.__dict__)  # Now that .__slosts__ is defined, 'Point2' object has no attribute '__dict__' error popped

# print(asizeof.asizeof(point2))  # 112 bytes of memory being used, significantly less


# point2.z = 5

# # print(point2.z) # The use of __slots__ does not allow dynamically create attributes /: 'Point2' object has no attribute 'z' error popped


'''
    Warning: 
        A word of caution is in order, as many of Python's built-in mechanisms implicitly assume that objects have the .__dict__ attribute. 
        When you use .__slots__(), then you waive that assumption, which means that some of those mechanisms might not work as expected anymore.
'''






'Making a Class an Iterable'

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __iter__(self): # The .__iter__() method is a generator function that returns an iterator
#         yield from (self.x, self.y)



# print(list(Point(4, 8)))    # [4,8] / The call to list() iterates over the attributes .x, .y, and .z, returning a list object. You don’t need to call .__iter__() directly.



'More examples with Class Methods applied: from_sequence & from_dict class methods'

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __iter__(self):
#         yield from (self.x, self.y)
    
#     def __str__(self):
#         return f'Point(x={self.x}, y={self.y})'

    
#     @classmethod
#     def from_sequence(cls, seq):
#         return cls(*seq)
    
#     @classmethod
#     def from_dict(cls, dic):
#             return cls(**dic)

#         # if 'x' in dic.keys() and 'y' in dic.keys():
#             # return cls(dic['x'], dic['y'])



# tuple1 = (4, 8)
# dic1 = {'x':4, 'y':8}

# point1 = Point.from_sequence(tuple1)
# print(point1)   # Point(x=4, y=8)

# point2 = Point.from_dict(dic1)
# print(point2)   # Point(x=4, y=8)






'Use of dataclasses module'

# from dataclasses import dataclass

# @dataclass
# class Point:

#     x: int | float
#     y: int | float


#     @classmethod
#     def from_seq(cls, sequence):
#         return cls(*sequence)
    
#     @staticmethod
#     def show_intro():
#         print('Hey! this is a 2D point')


# '''
#     This new class implementation uses Python's @dataclass decorator to turn the regular class into a data class. 
#     Instead of defining an .__init__() method, you list the instance attributes with their corresponding types. 
#     The data class will take care of writing a proper initializer for you. Note that you don't define .__repr__() either.
# '''

# point1 = Point(1, 2)
# point2 = Point.from_seq((1.0, 2.0))

# print(point1)
# print(point2)
# print(point1 == point2)

# print(repr(point2))






'Use of enum module'

# from enum import Enum

# class WeekDay(Enum):

#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7

#     @classmethod
#     def fav_day(cls):
#         return cls.FRIDAY
    
#     # def __str__(self):
#     #     return f"Current day: {self.name}"


# print(WeekDay.fav_day())    
# print(WeekDay.WEDNESDAY)    # dot notation implemented
# print(WeekDay(1))           # call notation implemented
# print(WeekDay['SATURDAY'].value)    # dict notation implemented


# for day in WeekDay:         # __iter__ implemented
#     print(day.name, "->", day.value)






'MRO: Method Resolution Order'

'''
    If a Class inherits from different Classes that provides implementations
    for the same method, which method the child class will use?

    1st -> The current class
    2nd -> The Leftmost superclasses (like the first passed as argument)
    3rd -> The super class listed next from left to right, up to the last superclass
    4th -> The superclasses of inherited classes
    5th -> The object class
    
'''

class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass


D().method()    # B.method

                    # This is the order of inheritance
print(D.__mro__)    # (
                    # <class '__main__.D'>,
                    # <class '__main__.B'>,
                    # <class '__main__.C'>, 
                    # <class'__main__.A'>, 
                    # <class 'object'>
                    # )


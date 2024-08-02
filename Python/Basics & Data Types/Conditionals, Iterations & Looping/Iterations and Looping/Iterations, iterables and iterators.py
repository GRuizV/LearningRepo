'''
Break, Continue and Pass statements
'''

# nums = [x for x in range(6)]


# # break
# print('break example')
# for num in nums:

#     print(num)

#     if num >= 3:

#         break

#         print('higher than three')

#     print('Next one!')


# print('\n','------------','\n')

# # continue
# print('continue example')
# for num in nums:

#     print(num)

#     if num >= 3:

#         continue
    
#         print('higher than three')

#     print('Next one!')


# print('\n','------------','\n')

# # pass
# print('pass example')
# for num in nums:

#     print(num)

#     if num >= 3:

#         pass
    
#         print('higher than three')

#     print('Next one!')




'''
Else as a 'No-break' statement
'''


# nums = [x for x in range(4)]


# for num in nums:

#     print(num)

#     if num == 2: break

# else: 

#     print('hit no-break')



# # Else as no-break practical example
# def index_finder(seq, target):

#     for i,v in enumerate(seq):

#         if v == target:

#             break
        
#     else:

#         return -1
    
#     return i


# names = ['Corey', 'Rick', 'John']

# index_location = index_finder(names, 'Steve')

# print(f'The resulting index is {index_location}')





'''
Iteraing an iterable from an iterator
'''

# nums = [1, 2, 3, 4]

# i_nums = iter(nums)

# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums)) This time it will throw an StopIteration Exception



''' This is what a for loop does in the background'''

# while True:

#     try:
#         item = next(i_nums)
#         print(item)
    
#     except StopIteration:
#         break




'''
Creating an iterator object
'''

# class MyRange:

#     def __init__(self, start, end):
        
#         self.value = start
#         self.end = end

#     def __iter__(self):
#         return self
    

#     def __next__(self):

#         if self.value >= self.end:
#             raise StopIteration
        
#         current = self.value
#         self.value += 1
#         return current

        
# nums = MyRange(1,10)

# print(list(nums))




' Generators - iterators'


def my_range(start, end):

    current = start

    while current < end:

        yield current

        current += 1

print(list(my_range(1,10)))




'''
Corey Schafer problem

    Create an iterator Class and Generator that loops over a sentence separated by spaces

'''



'Class Iterator'

# class Sentence:

#     def __init__(self, str):

#         self.str = str

#         self.words = str.split()

#         self.count = 0

#         self.end = len(self.words)


    
#     def __iter__(self):

#         return self
    


#     def __next__(self):

#         if self.count >= self.end:

#             raise StopIteration
        
#         current = self.words[self.count]

#         self.count += 1

#         return current
    


# my_sentence = Sentence('The following is a test')


# for i in my_sentence:    print(i)




'Generator Iterator'


# def GSentence(str):

#   for word in str.split():

#     yield word


# my_sentence = GSentence('The following is a test')


# for i in my_sentence:    print(i)
''' UNDERSTANDING STRINGS '''

# to comment out something by shortcut (in my keyboard: ctrl + \key )

# message = ''' Hi
# there's something I don't like 
# and it's weird' ''' 

# print (message)

# greeting = 'Hello'

# name = 'Michael'

# message = f"{greeting}, {name}. Welcome!"



''' SLICING STRINGS '''

# my_list =     [0,  1, 2, 3, 4, 5, 6, 7, 8, 9]
# Asc.  Index  0,  1, 2, 3, 4, 5, 6, 7, 8, 9 
# Desc. Index -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 

# list[star:end:step]

# print (my_list[::2])



# sample_url = 'http://coreyms.com'
# print sample_url

# Reverse the url
# print (sample_url[::-1])

# Get the top level domain
# print (sample_url[-4:])

# Print the url without the http://
# print (sample_url[7::])

# Print the url without the http:// or the top level domain
# print (sample_url[7:-4])



''' .strip(), .split() and .join () Methods '''

# text = "   Maegor Targaryen was the cruel king   sdafsdf"

# text = text.strip("safd ")


# text = text.split()

# print(text)

# text = ' '.join(text)

# print(text)


''' join () method vs for in statement '''

# #  Say we want to join items from an iterable 
# # and could be multiple ways to do it but lets compare

# from timeit import default_timer as timer

# my_list = ['a'] * 10000000

# # For in statment

# start = timer()

# my_string = ''

# for i in my_list:

#     my_string += i

# stop = timer()

# print(stop - start)


# # join() method

# start = timer()

# my_list = ''.join(my_list)

# stop = timer()

# print(stop - start)



l = 'Hello'

print(f'{l:#^11}')
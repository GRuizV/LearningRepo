
# x = 10

# if x > 5:
#     raise Exception('number higher than 5')



'From Corey Schafer tutorial'


# l = [1,2,3]
# i = l[4]


# try:
#    l = [1,2,3]
#    i = l[4]

# except Exception:
#     pass




# try:
#    l = [1,2,3]
#    i = l[4] 

# except IndexError as e:
#     print(e)




# try:
#    l = [1,2,3,4,5]
#    i = l[4]     #Now, this was corrected

#    var = bad_var

# except IndexError as e:
#     print(e)

# except Exception as e:
#     print(e)




# try:
#    l = [1,2,3,4,5]
#    i = l[4]

#    var = 'bad_var'     #Now, this was corrected

# except IndexError as e:
#     print(e)

# except Exception as e:
#     print(e)

# else:
#     print(var)




# try:
#    l = [1,2,3,4,5]  
#    i = l[4]

#    var = bad_var    #intentionally it was made wrong to show finally

# except IndexError as e:
#     print(e)

# except Exception as e:
#     print(e)

# else:
#     print(var)

# finally:
#     print('This is the end of the code')



'assert expresion'

# def age_check(n):

#     assert n > 0, 'Non positives ages are not accepted'

   
# age_check(-4)








'------------'


#Excercises

''' 
Question 1: Perfect division function Write a function division() that accepts two arguments. 
The function should be able to catch an exception such as ZeroDivisionError, ValueError, or any unknown error you might come across when you are doing a division operation.'

'''


# def division():

#     try:
#         a = int(input('>>> Enter a: '))
#         b = int(input('>>> Enter b: ')) 

#         print(f'{a} / {b} = {a/b}')


#         ans = str(input('Do you want to keep dividing numbers? (Y/N)'))

#         while ans not in 'YN':

#             ans = str(input('Do you want to keep dividing numbers? (Y/N)'))
        
#         if ans == 'Y':

#             division()

#         else: 
#             print("Calculations finished")

    
#     except ZeroDivisionError as e:

#         print(e)

#     except Exception as e:

#         print(e)

#     finally:

#         print('Processing Completed')
   

# division()

'''
PRINT HACKERRANK LOGO
With variable Thickness (Odd-Numbered)

'''

thickness = 7
width = thickness*3

c= 'H'

#Top triangle

# for i in range(thickness//2):

#     print( c*i).rjust(width//2-1,'-')  +  c  +   (c*i).ljust(width//2-1,'-')


# print()


# #Bottom triangle

# for i in range(thickness,-1,-1):

#     print( (c*i).rjust(width//2-1,' ')  +  c  +   (c*i).ljust(width//2-1,' '))



# Bottom triangle (My original approach in the exercise)

r = range( thickness )

ind = -1

for i in r:

    print( ( ( c * r[ind] ) .rjust( thickness - 1 )  +  c  +   ( c * r[ind] ) .ljust( thickness - 1 ) ) )
   
    ind -= 1







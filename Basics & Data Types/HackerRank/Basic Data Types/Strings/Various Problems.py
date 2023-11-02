'''
Find Subtring
find how many times CDC appear in ABCDCDC

'''

# str1 = 'ABCDCDC'
# subs = 'CDC'

# str1_len = len(str1)

# subs_len = len(subs)


# count = 0

# for i in range(str1_len):

#     if subs in str1[i:i+subs_len] : count += 1


# print(count)




'''
PRINT HACKERRANK LOGO
WIth variable Thickness (Odd-Numbered)

'''

# thickness = 5
# c= 'H'


# #Top triangle

# for i in range(thickness):

#     print( ( c*i ).rjust( thickness - 1 )  +  c  +   ( c*i ).ljust( thickness - 1 ) )



# # first parallels columns

# for i in range( thickness + 1 ):   

#     print( ( c*thickness ).center( 2*(thickness) - 1 ) + ' '*(2*thickness+1) +( c*thickness ).center( 2*(thickness) - 1 )     ) 



# # Middle Belt 

# for i in range( thickness//2 + 1 ):

#     print( ( c*( 5*thickness ) ).center( 6*thickness - 1 ) )



# # Second parallels columns

# for i in range( thickness+1 ): 

#     print(  ( c*thickness ).center( 2*(thickness) - 1 ) + ' '*( 2*thickness + 1 ) + ( c*thickness ).center( 2*(thickness)-1 )     ) 



# #Bottom triangle (original)

# r = range(thickness)

# ind = -1

# for i in r:

#     print( ( ( c * r[ind] ) .rjust( thickness - 1 )  +  c  +   ( c * r[ind] ) .ljust( thickness - 1 ) ) .rjust( 6*thickness-1 )  )

#     ind -= 1




#Bottom triangle (option 2)
# This turned out to be more simplier solution

# for i in range(thickness-1, -1, -1):

#     print( ( ( c * i ) .rjust( thickness - 1 )  +  c  +   ( c * i ) .ljust( thickness - 1 ) ) .rjust( 6*thickness-1 )  )

    







'''
TEXT WRAP
You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w.


Sample Input 

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4


Sample Output 

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''


# s = 'ABCDEFGHIJKLIMNOQRSTUVWX'
# w = 4


# def wrap(string, max_width):

#     p1 = len(string)//max_width

#     p2 = 0

#     r = range (p1)

#     final_string=''


#     for i in r:

#         final_string += s[p2:p2+w]+'\n'

#         p2 += w

#     final_string += s[p2:]


#     return print(final_string)



# wrap(s,w)


'''

DESIGNER DOOR MAT

Mr. Vincent works in a door mat manufacturing company. 
One day, he designed a new door mat with the following specifications:

Mat size must be N x M. ( N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.


Sample Input 

Size: 7 x 21 


Sample Output 

---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------


5x15

------.|.------
---.|..|..|.---
----WELCOME----
---.|..|..|.---
------.|.------

'''

# n = 7

# m = 3*n

# char = '.|.'


# for i in range(n//2):
#     print(  (i*char).rjust(m//2-1,'-')   +   char   +    (i*char).ljust(m//2-1,'-')    )

# print('WELCOME'.center(m,'-'))


# range_width = range(n//2)
# index = -1


# # for i in range_width:  # Original bottom pyramid approach
# #     print(  (range_width[index]*char).rjust(m//2-1,'-')   +   char   +    (range_width[index]*char).ljust(m//2-1,'-')    )
# #     index -= 1


# for i in range(n//2 - 1, -1 , -1):    #Enhanced bottom pyramid apporach

#     print(  ( i * char ).rjust(m//2-1,'-')   +   char   +    ( i * char ).ljust(m//2-1,'-')    )
 



'''
STRING FORMATTING
Given an integer, n, print the following values for each i integer from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary


'''

# number = 17

# pad = len(f'{number:0b}')

# for i in range(1,number+1):

#     o = f'{i:0o}'

#     h = f'{i:0X}'

#     b = f'{i:0b}'

#     print (  f'{str(i).rjust(pad)} {o.rjust(pad)} {h.rjust(pad)}  {b.rjust(pad)}'  )







'''

ALPHABET RANGOLI

You are given an integer, N. 
Your task is to print an alphabet rangoli of size. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:




#size 3

5x9
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----




#size 5

9x17
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------


#size 7

13x25

------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
------------g------------




#size 10

19x37
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------



'''


# n = 3

# letters = 'abcdefghijklmnopqrstuvwxyz'

# # abcdefghij
# l = letters[:n]

# # jihgfedcba
# l2 = l[::-1]

# # abcdefghijj
# l3 = l+l[-1]


# ind = -1

# ind2 = 0


# if n == 1:

#     print(l)

# else:

#     for i in range(n):
        
#         print(   ( '-'.join( l2[ : ind2 ] ) ) .rjust( ( ( 4*n - 5 ) // 2 ) , '-' )   +    f'-{ l[ ind ] }-'  +  ( '-'.join( l3[ ind : -1 ] ) ) .ljust( ( ( 4*n - 5 ) // 2 ) ,'-' )       )

#         ind -=1
#         ind2 +=1
    


# ind3 = -1
# ind4 = 1


# if n == 1:

#     pass

# else:

#     for i in range(n-1):
        
#         print(   ( '-'.join(l2[:ind3-1:])  ) .rjust( ( (4*n-5)//2 ) ,'-' )   +    f'-{  l [ind4]  }-'  + (  '-'.   join(   l[ind4+1:]   )    )    .ljust( ( (4*n-5)//2 ) ,'-' )       )

#         ind3 -=1
#         ind4 +=1





'''
CAPITALIZE TEXT

i: 1 w 2 r 3g
o: 1 W 2 R 3g

i: 132 456 Wq  m e
o: 132 456 Wq  M E

i: hello   world  lol
o: Hello   World  Lol

i: q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M
o: Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M

i: chris alan
o: Chris Alan

'''

# n = 'hello   world  lol'
# s = ''


# # My Approach

# print(f'Ori string: {n}')

# for i in range(len(n)):

#     if i == 0 and n[i].isalpha() == True:

#         s += n[i].upper()
        


#     elif n[ i-1 ] == ' ' and n[i].isalpha() == True:
    
#         s += n[i].upper()
        

#     else: s += n[i]


# print(f'Mod string: {s}')



# #Alternate solution from 'Discussion':

# new_s = ' '.join( [ i.capitalize() for i in n.split(' ') ])    # Trully Elegant

# print(new_s)


'''
--------
'''


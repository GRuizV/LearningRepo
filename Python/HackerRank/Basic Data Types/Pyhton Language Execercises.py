'''
FIND THE RUNNER-UP SCORE!
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up. (Meaning the second greater)

#If something goes wrong in the test, I will check the constrains

'''


# n = 5

# # CASES

# arr = [2, 3, 6, 6, 5]
# # arr = [-7,-8,-10,-2,-3]

# arr = sorted(arr,key=None,reverse=True)

# score = 0
# count = 1

# # print(arr)

# # arr = [6, 6, 5, 3, 2]

# for i in arr:
#     comp = arr[count]
#     if i > comp:
#         score = comp
#         break
        
#     count +=1
        
        
# print(score)



'''
NESTED LISTS
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

'''

# list1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
# list1 = sorted(list1,key= lambda x: x[1])   #I yet still do not understand the Lambda functionality but it worked!

# # list1 = []

# # for i in range(int(input())):
        
# #         name = input()
# #         score = float(input())
# #         list1.append([name, score])


# comp = list1[0][1]
# student_parameter = []
# output_list = []

# for i in list1:
#     if i[1] > comp:
#             student_parameter = i[1]
#             break

# # This is the current List [['Tina', 37.2], ['Harry', 37.21], ['Berry', 37.21], ['Harsh', 39.0], ['Akriti', 41.0]]

# for i in list1:
#     if i[1] == student_parameter: output_list.append(i)


# output_list = sorted(output_list)

# for i in range(len(output_list)):
#     print(output_list[i][0])




'''
FINDING THE PERCENTAGE
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

* Preceding asterisk in a variable: https://scripteverything.com/what-does-asterisk-before-variable-name-mean-in-python/#:~:text=The%20asterisk%20is%20an%20operator,the%20contents%20of%20that%20variable.

    name, *line = 'Krishna 67 68 69'.split() -  means this  Krishna - ['67', '68', '69']

'''


# # Sample input
# # 3
# # Krishna 67 68 69
# # Arjun 70 98 63
# # Malika 52 56 60
# # Malika


# n = 3
    
# student_marks_1 = {
#     'Krishna':[67,68,69],
#     'Arjun':[70,98,63],
#     'Malika':[52,56,60],
# }

# # student_marks = {}
    
# # for i in range(n):
# #     name, *line = input().split()     #A preceding asterisk expands the elements within a variable, for more, check the article above
# #     scores = list(map(float, line))
# #     student_marks[name] = scores


# query_name = 'Malika'

# res = 0

# for i in student_marks_1[query_name]:
#     res += i

# res = res/len(student_marks_1[query_name])

# print(f'{res:.2f}')


'''
LISTS
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at i position .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

'''

#Sample Input
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


# n = int(input())

# orders = []

# for i in range(n):
#     orders.append(input())

# orders = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']


# output_list = []


# for i in range(len(orders)):

#     order = orders[i].split()

#     if 'insert' in order: output_list.insert(int(order[1]),int(order[2]))

#     if 'print' in order: print(output_list)

#     if 'remove' in order: output_list.remove(int(order[1]))

#     if 'append' in order: output_list.append(int(order[1]))

#     if 'sort' in order: output_list.sort()

#     if 'pop' in order: output_list = output_list[:-1]

#     if 'reverse' in order: output_list = output_list[::-1]


'''
String Validators
You are given a string .
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

'''

# .isalnum(), .isalpha(), .isdigit(), .islower(), .isupper()


# s = 'qA2'


# l1 = [ i for i in s if i.isalnum() == True]
# l2 = [ i for i in s if i.isalpha() == True]
# l3 = [ i for i in s if i.isdigit() == True]
# l4 = [ i for i in s if i.islower() == True]
# l5 = [ i for i in s if i.isupper() == True]

# if len(l1) > 0 : print(True)
# else: print(False)
# if len(l2) > 0 : print(True)
# else: print(False)
# if len(l3) > 0 : print(True)
# else: print(False)
# if len(l4) > 0 : print(True)
# else: print(False)
# if len(l5) > 0 : print(True)
# else: print(False)


# #This is the approach from another user in HackerRank

# for fct in ['alnum', 'alpha', 'digit', 'lower', 'upper']:
#         print(any([eval(f'char.is{fct}()') for char in s]))




'''
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.


For example, product(A, B) returns the same as ((x,y) for x in A for y in B).


print (list(product([1,2,3],repeat = 2)))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print (list(product([1,2,3],[3,4])))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]

A = [[1,2,3],[3,4,5]]

print (list(product(*A)))
# [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]


B = [[1,2,3],[3,4,5],[7,8]]

print (list(product(*B)))
 [(1, 3, 7), (1, 3, 8), (1, 4, 7), 
  (1, 4, 8), (1, 5, 7), (1, 5, 8), 
  (2, 3, 7), (2, 3, 8), (2, 4, 7), 
  (2, 4, 8), (2, 5, 7), (2, 5, 8), 
  (3, 3, 7), (3, 3, 8), (3, 4, 7), 
  (3, 4, 8), (3, 5, 7), (3, 5, 8)]

'''


# from itertools import product


# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# res = sorted(product(a,b))

# for i in res:
#     print(i,end=' ')




'''
Merge the Tools!

Consider the following:

A string, s, of length n where s = c0c1...cn-1.
An integer, k, where k is a factor of n.

We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. 
Then, use each ti to create string ui such that:

- The characters in ui are a subsequence of the characters in ti .
- Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. 
    In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui .
- Given s and k, print n/k lines where each line i denotes string ui.

'''


# s = 'AAABCADDE'

# k = 3

# tis = [ s[i*k:(i+1)*k] for i in range(int(len(s)/k)) ]

# uis = list()

# for i in range(len(tis)):

#     temp = list()

#     ui = str()

#     for j in range(len(tis[i])):

#         if tis[i][j] not in ui:

#             ui += tis[i][j]

#     uis.append(ui)

# print(uis)




'''
collections.Counter()

A counter is a container that stores elements as dictionary keys,
and their counts are stored as dictionary values.

Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

input 

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

'''

# from collections import Counter

# n = input()

# shoes = map(int,input().split())

# print(list(shoes))

# customers = list()


# print(shoes)


# for i in range(int(input())):

#     customers.append(list(map(int,input().split())))

# print(customers)



'implementation'
# shoes = [2, 3, 4, 5, 6, 7, 6, 5, 18, 8]    

# customers = [[6, 55], [6, 45], [6, 55], [4, 40], [18, 60], [10, 50]]

# shoes = Counter(shoes)

# balance = int()


# for i in customers:

#     if shoes[i[0]] > 0:

#         shoes[i[0]] -= 1

#         balance += i[1]

        
# print(balance)





'''
itertools.permutations()

You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.


'''

# from itertools import permutations

# s = 'HACK'
# k = 3

# if k != 0:
#     res = [''.join(x) for x in sorted(permutations(s,k))]


# else: 
#     res = [''.join(x) for x in sorted(permutations(s))]


# for i in res:

#     print(i)





'''
Polar Coordinates

You are given a complex z. Your task is to convert it to polar coordinates.

constrain
 - Given number is a valid complex number

find 'r' and 'phi'

'''
# from cmath import phase
# from math import sqrt


# z = complex(input())

# r = sqrt((z.real**2) + (z.imag**2))

# phi = phase(z)


# print(r)
# print(phi)





'''
DefaultDict Tutorial

'''
# from collections import defaultdict

# a = ['a', 'a', 'b', 'a', 'b']

# b =  ['a', 'b', 'c']




# n = list(map(int,input().split()))


# d = defaultdict(list)

# for i in range(n[0]):

#     d['A'].append(input())

# for i in range(n[1]):

#     d['B'].append(input())


# res = list()


# for i in d['B']:

#     temp = list()

#     if i in d['A']:

#         for n, j in enumerate(d['A']):

#             if i == j:

#                 temp.append(n+1)
        
#         res.append(temp)

#     else:

#         res.append([-1])


# for i in res:
    
#     print(' '.join(map(str,i)))





'''
collections.namedtuple()

'''

# from collections import namedtuple


# col = ['ID', 'MARKS', 'NAME', 'CLASS'] 

# base = [['1', '97', 'Raymond', '7'], ['2', '50', 'Steven', '4'], ['3', '91', 'Adrian', '9'], ['4', '72', 'Stewart', '5'], ['5', '80', 'Peter','6']]

# Student = namedtuple('Sutdent', col)

# students = [Student(*i) for i in base]

# grades_sum = sum([int(x.MARKS) for x in students])


# print(grades_sum)

# print(len(students))

# print(f'{grades_sum/len(students):0.2f}')





'''
Calendar Module

'''

# import calendar


# # My Solution

# n = '08 05 2015'

# n = list(map(int,n.strip().split()))

# res = calendar.weekday(n[2], n[0], n[1])

# print(n)

# if res == 0:

#     print('MONDAY')

# elif res == 1:

#     print('TUESDAY')

# elif res == 2:

#     print('WEDNESDAY')

# elif res == 3:

#     print('THURSDAY')

# elif res == 4:

#     print('FRIDAY')

# elif res == 5:

#     print('SATURDAY')

# elif res == 6:

#     print('SUNDAY')
    

'---------------'

# # Someone else's in HR

# import calendar

# month, day, year = map(int, input().split())    # Love this unpacking directly

# week_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']  

# day_name = calendar.weekday(year, month, day)

# print(week_days[day_name])  # Brilliant to use the return of the weekday function to directly input the week_days list as an index. Really like it





'''
Time Delta

'''

# import datetime

# d1 = 'Sun 10 May 2015 13:54:36 -0700'
# d2 = 'Sun 10 May 2015 13:54:36 -0000'

# d1 = 'Sat 02 May 2015 19:54:36 +0530'
# d2 = 'Fri 01 May 2015 13:54:36 -0000'


# #Converting raw strings into datetime objects ignoring timezone

# d1, d2 = d1.split(), d2.split()

# d1_time = list(map(int, d1[4].split(":")))
# d2_time = list(map(int, d2[4].split(":")))

# months = {'Jan' : 1 , 'Feb' : 2 , 'Mar' : 3 , 'Apr' : 4 , 'May' : 5 , 'Jun' : 6 , 'Jul' : 7 , 'Aug' : 8 , 'Sep' : 9 , 'Oct' : 10 , 'Nov' : 11 , 'Dec' : 12}

# dt1 = datetime.datetime(int(d1[3]), months[d1[2]], int(d1[1]), d1_time[0], d1_time[1], d1_time[2])

# dt2 = datetime.datetime(int(d2[3]), months[d2[2]], int(d2[1]), d2_time[0], d2_time[1], d2_time[2])



# #dealing with Timezones

# d1_tz, d2_tz = d1[5], d2[5]

# d1_timedelta = datetime.timedelta( hours=int(d1_tz[1:3]), minutes= int(d1_tz[3:]) )

# d1_utc = dt1

# if "-" in d1_tz:

#     d1_utc = dt1 + d1_timedelta

# else:

#     d1_utc = dt1 - d1_timedelta


# d2_timedelta = datetime.timedelta( hours=int(d2_tz[1:3]), minutes= int(d2_tz[3:]) )

# d2_utc = dt2

# if "-" in d2_tz:

#     d2_utc = dt2 + d2_timedelta

# else:

#     d2_utc = dt2 - d2_timedelta


# # print(d1_utc)
# # print(d2_utc)

# # print(d1_timedelta)
# # print(d2_timedelta)

# time_diff = abs(d1_utc-d2_utc)

# print((time_diff.days*24*3600)+(time_diff.seconds))





'''
Finding MBC Angle

'''

# import math

# ab = 10

# bc = 10

# ac = math.sqrt((ab**2) + (bc**2))

# mbc_ang = math.degrees(math.acos(((ac**2+bc**2-ab**2)/(2*ac*bc))))

# mbc_ang = round(mbc_ang)

# print(mbc_ang)





'''
OrderedDict()

'''

# from collections import OrderedDict



# items = OrderedDict()

# prices = dict()




# entry = ['BANANA FRIES 12','POTATO CHIPS 30','APPLE JUICE 10','CANDY 5','APPLE JUICE 10','CANDY 5','CANDY 5','CANDY 5','POTATO CHIPS 30']



# for i in entry:

#     item = i.split()

#     item_name = ' '.join(item[:-1])


#     if f'{item_name}' not in items:

#         items[f'{item_name}'] = 1
    
#     else:

#         items[f'{item_name}'] += 1




#     if f'{item_name}' not in prices:

#         prices[f'{item_name}'] = int(item[-1])




# bill = [(k, v*prices[k]) for k,v in items.items()]



# for i in bill:

#     print (f'{i[0]} {i[1]}')





'''
Company Logo

'''

# s = 'aabbbccde'

# # s = 'tctesvgnclzykpmbcqixlonfidpdjbynrcpxsjmucpeyormenrjbibafpzkquminfnnbizgbpxeovefuykjrcebfnntvyamkgykcnvjqxvnprwrarpcgrjoucywgfnbnysgwzymcxyachlpsglosflsubqhvobedbtzuqmvgyvrpeclcsoeemysuyuejpjtahnrzmebztrjtzhhjtqlmhttxdnjilqsqymmhjmlzikkdzasshfktbfsaozyhaduyqcufucqxxuksnfjaiwacvlyiimfrzyxwobrfoalhmowcobbpwuqpwvlstbngxjrebfnckbcagoacmfuzvmqxefiwqkgfwgghxbulvhqiaqewdmmizjfgyymchohejdpsnnpvmtgqzxkesnrikywoolootuuikapycpxhkrplyuhzhndxckbvaynkzreybomwuemxtgmrjxbysarlsemwambppmrumivznuaqskzgpamfsjwwrjvtwyqpainuyyfmwnegjlmanqwvshvpsbpeykfwykdumdgjlkuwoxwqctihfdwvxrefggsxmjtxmpdcigjertcxwennzyamqpahytneybgmdyupusarhemazvozdqurftdvbnavynrsdzxjebjrdatbkoezdgwznplqqzakozjecyewsidawuxfpusmeusantzdglridxnwvbgwjcaofbplnwyxtmwerskdzwhgxfdqbpfhymlgwtvqeehnnhwgklxqkdjgmfxvuxwwpmnqxsaiitfehhbqdyveqfrqjjfnggmhjrgldgctnhzrrqdtbunxxcuwibqkjdickhrtbznevczqoidnfmtaveysysrgbhctwxmevuutrwyriugtuvhuxkqapfjyplczgekxisffoivofobqmipqxzunlrrtcmaivvhbfjvgywwtqubwszqwjtskyuxljhinqrhcgddejurivukcspaazjjwwloreqlreqjifwsv'

# res = {c:s.count(c) for c in s }

# res = sorted(res.items(), key = lambda x: (-x[1], x[0]))

# print(res[:3])





'''
Piling Up!

'''

# blocks = [1,2,3,7,8]

# pile = list()

# if blocks[-1] >= blocks[0]:
#     pile.append(blocks[-1])
#     del blocks[-1]

# else:
#     pile.append(blocks[0])
#     del blocks[0]

# print(pile)
# print(blocks)

# for i in range(len(blocks)):

#     if blocks[-1] >= blocks[0] and blocks[-1] <= pile[i]:
#         pile.append(blocks[-1])
#         del blocks[-1]

#     elif blocks[0] <= pile[i]:
#         pile.append(blocks[0])
#         del blocks[0]
    
#     else:
#         print('Not possible')
#         break


# print(pile)




''' 
Triangle Quest 2
'''

# for i in range( 1, 3 + 1 ): 

#     print( ''.join( [str(x) for x in range(1,i+1)] + [str(x) for x in range(i-1,0,-1)] ) ) 




''' 
Iterables and Iterators
'''
# from itertools import combinations


# # base = ['a','a','c','d']
# # base = 'b b a b b b b b b b'.split()
# base = 'a a c d'.split()

# K = 2

# comb = list(combinations(base, K))
# count = sum('a' in combination for combination in comb)
# probability = count / len(comb)

# print(probability)




''' 
Maximize It!
'''

# import itertools

# M = 1000

# l1 = [3,5,4]
# l2 = [3,7,8,9]
# l3 = [5,5,7,8,9,10]

# l_main = [l1, l2, l3]

# # [(3, 3), (3, 7), (3, 8), (3, 9), (5, 3), (5, 7), (5, 8), (5, 9), (4, 3), (4, 7), (4, 8), (4, 9)]
# comb = itertools.product(*l_main)

# pow2_comb = [ list(map(pow, x, itertools.repeat(2))) for x in comb ]

# sum_p2_comb = list( map( lambda x: (sum(x) % M) , pow2_comb ) )

# print(max(sum_p2_comb))




''' 
xxx
'''

# # n = 10
# # n = 1000000000000
# # n = 10
# # n = 534802106762
# # n = 549382313570
# # n = 731869010806
# # n = 547602
# # n = 649606239668
# n = 725261545450

# # s = 'aba'
# # s = 'a'
# # s = 'abcac'
# # s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# # s = 'epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq'
# # s = 'aedbdaeaddadddcedcbbabdccbecaecaccdbebeeadadcaabbaabbaeeeecaddbcdecbbdccdebaaebecdaaabbcdeccbabaabce'
# # s = 'gfcaaaecbg'
# # s = 'bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc'
# s = 'bab'


# as_in_s = len([x for x in s if x == 'a'])
# a_in_s_remaining = len([x for x in s[:n%len(s)] if x == 'a'])

# res = as_in_s*(n//len(s)) + a_in_s_remaining

# print(res)




''' 
Athletes Sort
'''

# arr = [int(x) for x in '7 1 0 10 2 5 6 5 9 9 9 9 1 23 12'.split()]

# # [7, 1, 0]
# # [10, 2, 5]
# # [6, 5, 9]
# # [9, 9, 9]
# # [1, 23, 12]
# arr = [arr[:3], arr[3:6], arr[6:9], arr[9:12], arr[12:15]]

# k = 1

# arr = sorted(arr, key = lambda x: x[k])

# for i in arr: 
#     p = [str(x) for x in i]
#     print(' '.join(p))




''' 
Any() and All()
'''


# # Quickest way to check Palindromy 

# base = 1001

# ans = str(base) == str(base)[::-1]

# print(ans)


# # With a List

# l = [1, 1010, 000, 50, 212, 1001]

# ans = [True if str(x) == str(x)[::-1] else False for x in l]

# print(ans)



# _ = '_____________________________________________'




# n = list(map(int,'12 9 61 5 14 1001 11 000'.split()))

# # My way to check palindromes
# def is_palindrome(l):

#     ans = False

#     res = [True if str(l)[x] == str(l)[len(str(l))-1-x] else False for x in range(len(str(l))//2)]

#     ans = all(res)

#     return ans

# res = [is_palindrome(x) for x in n]


# print(any(res))




_ = 'ginortS'


# s = 'Sorting1234'


# # _____________________________________________


# # My first solution
# up_case = [char for char in s if str.isupper(char)]
# lo_case = [char for char in s if str.islower(char)]

# numbers = list()

# for i in s:

#     try:
#         numbers.append(int(i))
    
#     except: pass

# odds = [x for x in numbers if x%2 != 0]
# even = [x for x in numbers if x%2 == 0]

# res = map(sorted, (lo_case,up_case,odds,even))
# res = ''.join([str(i) for elem in res for i in elem])
# print(res)



# # _____________________________________________



# # HackerRank's alternative

# upper = sorted(''.join(x for x in s if x.isupper()))
# lower = sorted(''.join(x for x in s if x.islower()))
# odds = sorted(''.join(x for x in s if x in '13579'))
# even = sorted(''.join(x for x in s if x in '02468'))


# print(''.join(lower+upper+odds+even))




_ = 'Validating Email Addresses With a Filter'

# import string

# s = '@something.com'

# extention_valid = [x for x in string.ascii_letters]
# website_valid = extention_valid + ['0','1','2','3','4','5','6','7','8','9']
# usr_name_valid = website_valid + ['-', '_']

# print(usr_name_valid)

# usr_name = s[:s.find('@')]
# website_name = s[s.find('@')+1:s.find('.')]
# extention_name = s[s.find('.')+1:]

# print(all(chr in usr_name_valid for chr in usr_name))      
# print(all(chr in website_valid for chr in website_name))
# print(all(chr in extention_valid for chr in extention_name))



# # Implemented solution
# def fun(s):
    
#     extention_valid = [x for x in string.ascii_letters]
#     website_valid = extention_valid + ['0','1','2','3','4','5','6','7','8','9']
#     usr_name_valid = website_valid + ['-', '_']

#     usr_name = s[:s.find('@')]
#     website_name = s[s.find('@')+1:s.find('.')]
#     extention_name = s[s.find('.')+1:]
    
#     lens = [len(x) for x in [usr_name,website_name,extention_name]]
    
#     if (all(char in usr_name_valid for char in usr_name)) and (all(char in website_valid for char in website_name)) and (all(char in extention_valid for char in extention_name)) and len(extention_name) <= 3 and all(x>0 for x in lens):
#         return True
    
#     else:
#         return False






_ = 'xxxx'























































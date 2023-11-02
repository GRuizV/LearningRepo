
'Strings Manipulation - Making Anagrams'

# import collections

# a = 'cde'
# b = 'abc'

# # a = 'cde'
# # b = 'dcf'


# a_s = set(a)
# b_s = set(b)

# common = a_s.intersection(b_s)
# diff = [x for x in a_s.difference(b_s)] + [x for x in b_s.difference(a_s)]

# deletions = 0

# for i in common:
#     deletions += abs(a.count(i)-b.count(i))

# for i in diff:
#     deletions += a.count(i) + b.count(i)


# print(deletions)





'String Manipulation - Alternating Characters'

# s = ['AAAA', 'BBBBB', 'ABABABAB', 'BABABA', 'AAABBB']

# for str in s:

#     deleted = 0

#     i = 0
#     j = 1

#     while True:

#         if j == len(str): 
#             break       

#         if str[i] == str[j]:
#             deleted += 1
#             j += 1

#         else:
#             i = j
#             j += 1

#     print(deleted)




'String Manipulation - Sherlock and the Valid String'

# from collections import Counter

# s = 'abcdefghhgfedecba'

# s = Counter(s)

# val = sorted(s.values())

# def test(s):
#     res = all( [x == s[0] for x in s] ) 
#     return res

# if test(val):
#     print('YES')

# elif test(val[1:]):  
#     print('YES')

# else:

#     val[-1]-=1
#     if test(val):        
#         print('YES')

#     else:       
#         print('NO')




'String Manipulation - Special String Again'


# # My solution worked but wasn't scalable enough

# s = 'mnonopoo'


# def is_special(s): 
    
#     test1 = False
#     test2 = False

#     if all(x == s[0] for x in s):
#         test1 = True

#     if len(s) > 1 and len(s)%2 != 0 and all(x == s[0] for x in s[0:len(s)//2]+s[len(s)//2+1:]):
#         test2 = True

#     if test1 or test2:
#         return True
    
#     else:
#         return False


# def subs_gen(s):

#     subs = list()
   
#     for i in range(1, len(s)+1):
        
#         for j in range( (len(s)+1) - i ):

#             subs.append(s[j:j+i])
    
#     res = [x for x in subs if is_special(x)]

#     return res


# print(subs_gen(s))


'--------------------------------------------'


# #Some other guy's solution

# def substrCount(n, s):

#     nsubs, nchars, ch = 1, 1, s[0]

#     for i in range(1,n):

#         if ch == s[i]:

#             nchars += 1
#             nsubs += nchars

#         else:

#             for j in range(i+1, min(n, i+1+nchars)):

#                 if s[j] != ch:                    
#                     break

#                 nsubs += 1

#             ch, nchars = s[i], 1

#             nsubs += 1

#     return nsubs




'String Manipulation - Common Child'



# s1 = 'SHINCHAN'
# s2 = 'NOHARAAA'


'--------------------------------------------'

# # My solution worked on 2 of the 3 run cases. 

# ind_1 = int()
# res = list()
# ind_2 = int()
# child = str()
# i = int()


# while i <= len(s1):

#     if i == len(s1):
#         break

#     j = 0    

#     if ind_2 != 0 or s2[ind_2] in child:  # And s1[ind2] not in child
#         j = ind_2 + 1

#     while j < len(s2):
        
#         if s1[i] == s2[j]:
            
#             if ind_2 == 0 and s2[ind_2] not in child: # And s1[ind2] not in child
#                 ind_1 = i  

#             child += s1[i]
#             ind_2 = j
#             break
        
#         j += 1
    
#     i += 1

#     if i == len(s1):

#         res.append([child, ind_1])
#         child = str()
#         i = ind_1 + 1
#         ind_2 = 0

# res = sorted(res, key = lambda x: len(x[0]))

# sol = len(res[-1][0])

# print(res)
# print(sol)



'--------------------------------------------'


#Some other guy's solution

# This problem was resolved by this guy using an application of the LCS (Longest Common Substring) Algorithm


# s1 = 'SHINCHAN'
# s2 = 'NOHARAAA'


# prev = [-1 for i in range(len(s2)+1)]

# for i in range(len(s1),-1,-1):

#     curr = [-1 for i in range(len(s2)+1)]

#     for j in range(len(s2),-1,-1):

#         if i==len(s1) or j==len(s2):

#             curr[j] = 0

#         else:

#             if s1[i]==s2[j]:
#                 curr[j] = 1 + prev[j+1]

#             else:
#                 curr[j] = max(prev[j], curr[j+1])

#     prev = curr

# print(prev)




'String Manipulation - Hash Table: Ransom Notes'


# m = 'ive got a lovely bunch of coconuts'
# n = 'ive got some coconuts'

# dict_n1 = {k:n.count(k) for k in n.split()} # What I need
# dict_n2 = {k:m.count(k) for k in n.split()} # What I count with



# #This was my first solution
# # print(list(zip(dict_n1.values(), dict_n2.values())))

# x = all([x[0]<=x[1] for x in zip(dict_n1.values(), dict_n2.values())])

# # print(dict_n1)
# # print(dict_n2)

# print('Yes') if x else print('No')




# # This was my second solution
# res = sorted(list(map(lambda x: x[1]-x[0],zip(dict_n1.values(),dict_n2.values()))))

# print('Yes') if res[0] >= 0 else print('No')




# # This solution came from ChatGPT

# dict_n1 = {k:n.count(k) for k in n.split()} # What I need
# dict_n2 = {k:m.count(k) for k in m.split()} # What I count with

# res = True

# for word, count in dict_n1.items():
#     if word not in dict_n2 or dict_n2[word] < count:
#         res = False

# print('Yes') if res else print('No')

# # At the very end of the exercise, this strategy of accessing the word in the second dictionary was key but also importing Counter from collections since..
# # the first two comprehensions still were consuming resources.
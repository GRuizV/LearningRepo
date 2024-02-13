
'1. Two Sum'

# # 1st approach
# nums = [3,2,4]
# target = 6
# result = []

# for i in range(len(nums)):

#     for j in range(i+1, len(nums)):

#         if nums[i] + nums[j] == target:
#             result = [i, j]
#             break
        
#     if result:
#         break
     
# print(result)


# # 2nd approach
# nums = [3,2,4]
# target = 6
# hashmap = {v:k for k,v in enumerate(nums)}
# result = []

# for i in range(len(nums)):

#     comp = target - nums[i]

#     if comp in hashmap and i != hashmap[comp]:
#         result = [i, hashmap[comp]]
#         break
   
 
# print(result)


# # 3rd approach
# nums = [3,2,4]
# target = 6
# hashmap = {}
# result = []

# for i in range(len(nums)):

#     comp = target - nums[i]

#     if comp in hashmap:
#         result = [i, hashmap[comp]]
#         break

#     hashmap[nums[i]] = i
    
# print(result)




'2. Add Two Numbers'


# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Input
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))


# # LeetCode Editorial solution
# def addTwoNumbers(l1, l2):

#     dummyHead = ListNode(0)

#     curr = dummyHead

#     carry = 0

#     while l1 != None or l2 != None or carry != 0:

#         l1Val = l1.val if l1 else 0
#         l2Val = l2.val if l2 else 0

#         columnSum = l1Val + l2Val + carry

#         carry = columnSum // 10

#         newNode = ListNode(columnSum % 10)

#         curr.next = newNode
#         curr = newNode

#         l1 = l1.next if l1 else None
#         l2 = l2.next if l2 else None

#     return dummyHead.next

# result = addTwoNumbers(l1, l2)



# # My version of the solution

# # 1st list processing
# l1_list = []
# l1_next_node = l1

# while l1_next_node is not None:

#     l1_list.append(l1_next_node.val)
#     l1_next_node = l1_next_node.next

# l1_num = str()

# for num in l1_list:
#     l1_num += str(num)

# l1_num = int(l1_num[-1::-1])


# # 2nd list processing
# l2_list = []
# l2_next_node = l2

# while l2_next_node is not None:

#     l2_list.append(l2_next_node.val)
#     l2_next_node = l2_next_node.next

# l2_num = str()

# for num in l2_list:
#     l2_num += str(num)

# l2_num = int(l2_num[-1::-1])


# # Result outputting

# lr_num = l1_num + l2_num
# lr_str = str(lr_num)[-1::-1]

# lr_llist = ListNode()
# curr = lr_llist

# for i in lr_str:

#     new_node = ListNode(i)

#     curr.next = new_node
#     curr = new_node


# # Validating
# while lr_llist is not None:
#     print(lr_llist.val)
#     lr_llist = lr_llist.next




'3. Longest Substring Without Repeating Characters'

# s = "abcabcbb"


# # My solution
# substrings = []

# i = 0

# while i < len(s):

#     sub = str()

#     for char in s[i:]:

#         if char in sub:
#             substrings.append(sub)
#             break

#         sub += char
    
#     if sub not in substrings:
#         substrings.append(sub)

#     i += 1

# # print(substrings)

# max_sub = max(substrings, key = len) if substrings else 0

# # print(max_sub)

# print(max_sub, len(max_sub))


# # Another more efficient solution

# def lengthOfLongestSubstring(s: str) -> int:
        
#         n = len(s)
#         maxLength = 0
#         charMap = {}
#         left = 0
        
#         for right in range(n):

#             if s[right] not in charMap or charMap[s[right]] < left:
#                 charMap[s[right]] = right
#                 maxLength = max(maxLength, right - left + 1)

#             else:
#                 left = charMap[s[right]] + 1
#                 charMap[s[right]] = right
        
#         return maxLength


# lengthOfLongestSubstring(s)




'4. Median of Two Sorted Arrays'

# # Input
# nums1 = [1,3]
# nums2 = [2]


# # My Approach
# nums_total = sorted(nums1 + nums2)

# if len(nums_total) % 2 != 0:
    
#     median_idx = len(nums_total) // 2 
#     median = float(nums_total[median_idx])
#     print(f'{median:.5f}')

# else:
#     median_idx = len(nums_total) // 2 
#     print(nums_total[median_idx-1], nums_total[median_idx] )
#     median = (nums_total[median_idx-1] + nums_total[median_idx]) / 2
#     print(f'{median:.5f}')


'''
Note: My solution actually worked, but don't know why is not working in LeetCode.
        Apparently, they want a solution with mergesort.
'''


# # Mergesort Solution with pointers
# def findMedianSortedArrays(nums1, nums2) -> float:
        
#         m, n = len(nums1), len(nums2)
#         p1, p2 = 0, 0
        
#         # Get the smaller value between nums1[p1] and nums2[p2].
#         def get_min():
#             nonlocal p1, p2
#             if p1 < m and p2 < n:
#                 if nums1[p1] < nums2[p2]:
#                     ans = nums1[p1]
#                     p1 += 1
#                 else:
#                     ans = nums2[p2]
#                     p2 += 1
#             elif p2 == n:
#                 ans = nums1[p1]
#                 p1 += 1
#             else:
#                 ans = nums2[p2]
#                 p2 += 1
#             return ans
        
#         if (m + n) % 2 == 0:
#             for _ in range((m + n) // 2 - 1):
#                 _ = get_min()
#             return (get_min() + get_min()) / 2
#         else:
#             for _ in range((m + n) // 2):
#                 _ = get_min()
#             return get_min()
        
# print(findMedianSortedArrays(nums1, nums2))

'''
Note: Honestly I feel this is kind of ego lifting.
'''




'5. Longest Palindromic Substring'

# # Input
# s = "cbbd"


# # 1st Approach: Brute Force

# # Creating the possible substrings from the input
# subs = []

# for i in range(1, len(s)+1):
    
#     for j in range((len(s)+1)-i):

#         subs.append(s[j:j+i])

# # # validating
# # print(subs)        

# palindromes = sorted(filter(lambda x : True if x == x[::-1] else False, subs), key=len, reverse=True)

# print(palindromes)

'''
Note: While the solution works, is evidently not efficient enough / Time Limit Exceeded.
'''


# # 2nd Approach: Same brute force but less brute

# max_len = 1
# max_str = s[0]

# for i in range(len(s)-1):

#     for j in range(i+1, len(s)):

#         sub = s[i:j+1]        

#         if (j-i)+1 > max_len and sub == sub[::-1]:

#             max_len = (j-i)+1
#             max_str = s[i:j+1]


# print(max_str)




'7. Reverse Integer'

# # Input
# x = -15

# # My Solution
# raw_res = str(x)[::-1]

# if '-' in raw_res:
#     res = int(raw_res[:-1])
#     res = int('-'+str(res))

# else:
#     res = int(raw_res)


# min_32bit = -2**31
# max_32bit = 2**31-1

# if res > max_32bit or res < min_32bit:
#     print(0)

# else:
#     print(res)




'8. String to Integer (atoi)'

#Input
# s = "   -43.25"


# # My approach

# # Cleaning leading blank spaces
# s = s.strip()

# # In case of a sign present
# sign = None

# if s[0] == '-' or s[0] == '+':    
#     sign = s[0]
#     s = s[1:]


# num = ''

# # Reviewing each valid character
# for char in s:    
#     if char not in '0123456789.':
#         break    
#     num += char


# decimals = None

# # In case of a decimals
# if '.' in num:
#     decimals = num[num.find('.')+1:] #35
#     num = num[:num.find('.')]   #42
#     decimal_break = 5 * 10**(len(decimals)-1)

#     decimals = int(decimals)
    
#     #in case no number befor '.'
#     if not num:
#         num = 0
#     else:
#         num = int(num)
    
#     if decimals >= decimal_break:
#         num += 1

# elif num:
#     num = int(num)



# # In case is negative
# if sign == '-':
#     num = int('-'+str(num))


# max_32bit = 2**31-1
# min_32bit = -2**31


# #Outputting the result
# if not num:
#     print(0)

# else:
 
#     if num < min_32bit:
#         print(min_32bit)

#     elif num > max_32bit:
#         print(max_32bit)
    
#     else:      
#         print(num)

''' 
Note:
    It leaved cases unhandled. I also don't have the time to keep building the solution.
'''

# # ChatGPT approach

# def atoi(s: str) -> int:
#     s = s.strip()  # Remove leading and trailing whitespace
#     if not s:
#         return 0
    
#     sign = 1
#     i = 0
    
#     # Check for sign
#     if s[i] in ['+', '-']:
#         if s[i] == '-':
#             sign = -1
#         i += 1
    
#     # Iterate through characters and build the number
#     num = 0
#     while i < len(s) and s[i].isdigit():
#         num = num * 10 + int(s[i])
#         i += 1
    
#     # Apply sign and handle overflow
#     num *= sign
#     num = max(-2**31, min(2**31 - 1, num))
    
#     return num

# print(atoi(s))




'11. Container With Most Water'

# # Input
# heights = [1,8,6,2,5,4,8,3,7]


# # My Approach
# max_area = 0

# for i in range(len(heights)):

#     for j in range(i+1, len(heights)):

#         height = min(heights[i], heights[j])
#         width = j-i
#         area = height * width

#         max_area = max(max_area, area)

# print(max_area)


'''
Note:
    While this approach works, its complexity goes up to O(n), and is required to be more efficient
'''


# # Two-pointer solution

# left = 0
# right = len(heights)-1
# max_area = 0

# while left < right:

#     h = min(heights[left], heights[right])
#     width = right - left
#     area = h * width

#     max_area = max(max_area, area)

#     if heights[left] <= heights [right]:
#         left += 1
    
#     else:
#         right -= 1


# print(max_area)




'13. Roman to Integer'

'''
Substraction exceptions:
    - I can be placed before V (5) and X (10) to make 4 and 9. 
    - X can be placed before L (50) and C (100) to make 40 and 90. 
    - C can be placed before D (500) and M (1000) to make 400 and 900.
'''

# # Input
# s = 'MCMXCIV'


# # My approach
# res = 0
# rom_to_int_dic = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000, }


# #Substraction Exceptions
# if 'IV' in s:
#     res += rom_to_int_dic['IV']
#     s = s.replace('IV','')

# if 'IX' in s:
#     res += rom_to_int_dic['IX']
#     s = s.replace('IX','')

# if 'XL' in s:
#     res += rom_to_int_dic['XL']
#     s = s.replace('XL','')

# if 'XC' in s:
#     res += rom_to_int_dic['XC']
#     s = s.replace('XC','')

# if 'CD' in s:
#     res += rom_to_int_dic['CD']
#     s = s.replace('CD','')

# if 'CM' in s:
#     res += rom_to_int_dic['CM']
#     s = s.replace('CM','')

# # Dealing with the Remaining Number
# if s:
#     for chr in s:
#         res += rom_to_int_dic[chr]

# else:
#     print(res)


# print(res)

'''
Note: This version works, but there is a more concise one
'''

# s = 'MCMXCIV'

# # ChatGPT's Approach
# roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# total = 0
# prev_value = 0

# for char in s[::-1]:    #Reverse to simplify the process
    
#     curr_value = roman_dict[char]

#     if curr_value < prev_value:
#         total -= curr_value
    
#     else:
#         total += curr_value
#         prev_value = curr_value

# print(total)




'13.1 Roman to Integer - Variation: the other way around, Just For Fun.'

# # Input
# num = 1994

# # Ref
# rom_to_int_dic = {
#     'I': 1,
#     'IV': 4,
#     'V': 5,
#     'IX': 9,
#     'X': 10,
#     'XL': 40,
#     'L': 50,
#     'XC': 90,
#     'C': 100,
#     'CD': 400,
#     'D': 500,
#     'CM': 900,
#     'M': 1000,
# }

# '''
# Substraction exceptions:
#     - I can be placed before V (5) and X (10) to make 4 and 9. 
#     - X can be placed before L (50) and C (100) to make 40 and 90. 
#     - C can be placed before D (500) and M (1000) to make 400 and 900.
# '''

# # My approach
# s = ''

# while num > 0:

#     if num / 1000 >= 1:
#         s = s + 'M'
#         num -= 1000

#     elif num / 900 >= 1:
#         s = s + 'CM'
#         num -= 900

#     elif num / 500 >= 1:
#         s = s + 'D'
#         num -= 500

#     elif num / 400 >= 1:
#         s = s + 'CD'
#         num -= 400
        
#     elif num / 100 >= 1:
#         s = s + 'C'
#         num -= 100

#     elif num / 90 >= 1:
#         s = s + 'XC'
#         num -= 90

#     elif num / 50 >= 1:
#         s = s + 'L'
#         num -= 50

#     elif num / 40 >= 1:
#         s = s + 'XL'
#         num -= 40

#     elif num / 10 >= 1:
#         s = s + 'X'
#         num -= 10
    
#     elif num / 9 >= 1:
#         s = s + 'IX'
#         num -= 9
    
#     elif num / 5 >= 1:
#         s = s + 'V'
#         num -= 5
    
#     elif num / 4 >= 1:
#         s = s + 'IV'
#         num -= 4
    
#     elif num / 1 >= 1:
#         s = s + 'I'
#         num -= 1

# print(s, num)


'''
Note: Again, this version works, but there is a more concise one
'''

# # ChatGPT's Approach

# # Input
# num = 1994
# res = ''

# inv_roman_dict = {
#     1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
#     90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
# }

# for value, symbol in sorted(inv_roman_dict.items(), reverse=True):
    
#     while num >= value:
        
#         res = res + symbol
#         num -= value
    
# print(res)




'xxx'

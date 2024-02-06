
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




'xxx'




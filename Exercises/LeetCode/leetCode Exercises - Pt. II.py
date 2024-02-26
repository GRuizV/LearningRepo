'20. Valid Parentheses'

# input / Case - expected result
# s = '()'    # True
# s = '()[]{}'    # True
# s = '(]'    # False
# s = '([({[]{}}())])'    # True
# s = '([({[)]{}}())])'    # False
# s = '))'    # False
# s = '(('    # False



# My approach

# def isValid(s):

#     stack = list(s)
#     temp = []
#     dic = {'(': ')', '[':']', '{':'}'}  

#     while True:

#         if len(stack) == 0 and len(temp) != 0:
#             return False

#         popped = stack.pop(-1)

#         if popped in '([{':
            
#             if len(temp) == 0 or temp[0] != dic[popped]:
#                 return False
                            
#             else:                
#                 temp = temp[1:]

#         else:
#             temp.insert(0,popped)

#         if len(stack) == 0 and len(temp)==0:
#             return True
        


# print(isValid(s))

'Notes: it works!'




'21. Merge Two Sorted Lists'


# Base
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Input

# 1st Input
# #List 1
# one1, two1, three1 = ListNode(1), ListNode(2), ListNode(4)
# one1.next, two1.next = two1, three1

# #List 2
# one2, two2, three2 = ListNode(1), ListNode(3), ListNode(4)
# one2.next, two2.next = two2, three2


# 2nd Input
# #List 1
# one1, two1, three1 = ListNode(4), ListNode(3), ListNode(4)
# one1.next, two1.next = two1, three1

# #List 2
# one2, two2, three2 = ListNode(1), ListNode(0), ListNode(50)
# one2.next, two2.next = two2, three2






#My Approach
# def mergeTwoLists(list1:ListNode, list2:ListNode) -> ListNode:

#     if list1.val == None and list2.val != None:
#         return list2
    
#     if list2.val == None and list1.val != None:
#         return list1
    
#     if list1.val == None and list2.val == None:
#         return ListNode(None)


#     head = ListNode()
#     curr_res = head

#     curr1, curr2 = list1, list2

#     while True:

#         if curr1 != None and curr2 != None:
            
#             if curr1.val <= curr2.val:
#                 curr_res.next = curr1
#                 curr_res = curr_res.next
#                 curr1 = curr1.next     
                
#             else:
#                 curr_res.next = curr2
#                 curr_res = curr_res.next
#                 curr2 = curr2.next                   

#         elif curr1 != None:
#             curr_res.next = curr1
#             curr_res = curr_res.next
#             curr1 = curr1.next

#         elif curr2 != None:
#             curr_res.next = curr2
#             curr_res = curr_res.next
#             curr2 = curr2.next
        

#         if curr1 == None and curr2 == None:
#             break


#     return head.next


# res = []
# res_node = mergeTwoLists(one1, one2)

# while res_node != None:

#     res.append(res_node.val)
#     res_node = res_node.next


# print(res)

'Notes: it works!'




'22. Generate Parentheses'

#Input
# n = 3   # Expected Output: ['((()))', '(()())', '(())()', '()(())', '()()()']

# # My Approach
# def generateParenthesis(n):
 
#     if n == 1:
#         return ['()']

#     result = []

#     for i in generateParenthesis(n-1):
#         result.append('('+ i +')')
#         result.append('()'+ i )
#         result.append(i + '()')


#     return sorted(set(result))

# print(generateParenthesis(4))

'''
Note: 
    My solution kind of work but it was missing one variation, apparently with DFS is solved.
'''


# # DFS Approach

# def generateParenthesis(n):
    
#     res = []

#     def dfs (left, right, s):

#         if len(s) == 2*n:
#             res.append(s)
#             return

#         if left < n:
#             dfs(left+1, right, s + '(')

#         if right < left:
#             dfs(left, right+1, s + ')')

#     dfs(0,0,'')

#     return res


# print(generateParenthesis(4))




'xxx'
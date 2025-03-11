from typing import List, Optional

'''
Snippets Index

- Roman to Integer & Integer to Roman case.
- All permutations from a iterable. (RC)
- Kadane's Algorithm (DP)
- LeetCode Challenge #62. Unique Paths (DP)
- Floyd's Cycle Detection Algorithm (TP)
- How to reverse a Linked Lists
- How to capture coordinates in a Matrix (Matrix)
- Fibonacci with Memoization and Dynamic Porgramming (DP)
- Levenshtein Distance (DP)
- Function to manage API responses with pagination (BackEnd)
- How to store all paths in a BST (DFS)



*RC: Recursion
*DP: Dynamic Programming
*TP: Two-pointers
*DFS: Depth-First Search

(10)

'''

"""UTILS"""
# Binary Tree Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# List Node Definition
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Pretty Print Function
def pretty_print_bst(node:TreeNode, prefix="", is_left=True):

    if not node:
        return

    if node.right is not None:
        pretty_print_bst(node.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    if node.left is not None:
        pretty_print_bst(node.left, prefix + ("    " if is_left else "│   "), True)




"""SNIPPETS"""

'''Roman to Integer & Integer to Roman case'''
# def x():
#     # Roman to Integer
#     s = 'MCMXCIV'

#     # ChatGPT's Approach
#     roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     total = 0
#     prev_value = 0

#     for char in s[::-1]:    #Reverse to simplify the process
        
#         curr_value = roman_dict[char]

#         if curr_value < prev_value:
#             total -= curr_value
        
#         else:
#             total += curr_value
#             prev_value = curr_value

#     print(total)



#     # Integer to Roman
#     num = 1994
#     res = ''

#     inv_roman_dict = {
#         1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
#         90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
#     }

#     for value, symbol in sorted(inv_roman_dict.items(), reverse=True):
        
#         while num >= value:
            
#             res = res + symbol
#             num -= value
        
#     print(res)

'''All permutations from a iterable'''
# def x():
#     nums = [1,2,3,4]

#     def permutations(nums):

#         if len(nums) == 0:
#             return []
        
#         if len(nums) == 1:
#             return [nums]
        
#         lst = []

#         for i in range(len(nums)):

#             num = nums[i]
#             rest = nums[:i] + nums[i+1:]

#             for perm in permutations(rest):
#                 lst.append([num] + perm)

#         return lst

#     print(permutations(nums))

'''Kadane's Algorithm (Dynamic Programming)'''
# def x():
#     '''
#     This algorithm designed by Joseph Kadane solves quite efficiently the problem
#     of finding a subsegment that fits a max or minimum (or any other criteria for that matter)
#     '''

#     nums = [-2,1,-3,4,-1,2,1,-5,4]
#     # Output: 6 / [4,-1,2,1]

#     def kadanes(nums):

#         max_ending_here = max_so_far = nums[0]

#         for num in nums[1:]:

#             max_ending_here = max(num, max_ending_here + num)
#             max_so_far = max(max_so_far, max_ending_here)
        
#         return max_so_far

#     print(kadanes(nums))    # Output: 6

'''62. Unique Paths - 1st Dynamic Programming Problem - LeetCode Challenge'''
# def x():
    
#     '''
#     Notes:

#     The basis of the Dynamic Programming is to "Cache" a solution and store it into a grid to later use it
#     to save computing resources.

#     The grid is populated by 1's and summing to the right and down, the bottom right cell will hold the total number of unique ways to get there.

#     ------------------------------------------------------------------------------------

#     This problem was pretty similar to the one on Turing's tests, althought here is requested
#     to find a bigger scale of thar problem. The classic 'How many ways would be to get from x to y',

#     if the problem were only set to m = 2, it'd be solved with fibonacci, but sadly that was not the case,
#     here, Dynamic Programming was needed.

#     The problem is graphically explained here: https://www.youtube.com/watch?v=IlEsdxuD4lY

#     But the actual answer I rather take it from the leetCode's solutions wall, since is more intuitive to me.

#     '''

#     # Input
#     # Case 1:
#     m, n = 3, 7
#     # Output: 28

#     # Case 2:
#     m, n = 3, 2
#     # Output: 3


#     # Solution
#     def uniquePaths(m: int, n: int) -> int:

#         # Handling the corner case in which any dimention is 0
#         if n == 0 or m == 0:
#             return 0


#         # Here the grid is initialized
#         result = [[0]*n for _ in range(m)]

#         # The first column of the grid is set to 1, since there is only (1) way to get to each cell of that column
#         for row in range(m):
#             result[row][0] = 1

#         # The first row of the grid is set to 1, since there is only (1) way to get to each cell of that row
#         for col in range(n):
#             result[0][col] = 1


#         # Here all the grid is traversed summing up the cells to the left and up, since are the only ways to get to the current cell
#         # The range starts in 1 since all the first column and row are populated, so the traversing should start in [1,1]
#         for i in range(1, m):

#             for j in range(1, n):

#                 result[i][j] = result[i-1][j] + result[i][j-1]
        

#         # The bottom right cell will store all the unique ways to get there
#         return result[-1][-1]
    
#     # print(uniquePaths(m, n))

'''Floyd's Cycle Detection Algorithm (Two-Pointers)'''
# def x():

#     '''
#     also known as the "tortoise and hare" algorithm, is a pointer algorithm that uses two pointers moving at different speeds to detect cycles in a sequence of values.
#     '''

#     nums = [-2,1,-3,4,-1,2,1,-5,4]
#     # Output: 6 / [4,-1,2,1]


#     def floyd_cycle_detection(seq):

#         def next_value(x):
#             # This function should return the next value in the sequence.
#             # You need to define this based on your specific problem.
#             pass

#         slow = seq
#         fast = seq

#         while True:
#             slow = next_value(slow)
#             fast = next_value(next_value(fast))
            
#             if slow == fast:
#                 break

#         # Find the start of the cycle
#         slow = seq
#         while slow != fast:
#             slow = next_value(slow)
#             fast = next_value(fast)

#         return slow  # This is the start of the cycle

#     floyd_cycle_detection(seq=nums)

'''How to reverse a Linked Lists'''
# def x():
#     class ListNode:
#         def __init__(self, val=0, next=None):
#             self.val = val
#             self.next = next


#     def reverseList(head:ListNode) -> ListNode:
        
#         # Initialize node holders
#         prev = None
#         curr = head    

#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node       
        
#         return prev


#     def rec_reverseList(head:ListNode) -> ListNode:
        
#         # Base case
#         if not head or not head.next:
#             return head   

#         # Recursive Call
#         new_head = rec_reverseList(head.next)

#         # Reversing the list
#         head.next.next = head
#         head.next = None

#         return new_head

'''How to capture coordinates in a Matrix'''
# def x():
#     board = [["o","x","x","o"],["o","o","x","x"],["x","x","x","x"],["x","x","x","o"]]

#     coordinates = []

#     for i, row in enumerate(board):
#         coordinates.extend([(i,j) for j,elem in enumerate(row) if board[i][j] == 'o'])

#     # [(0, 0), (0, 3), (1, 0), (1, 1), (3, 3)]
#     print(coordinates)

'''Fibonacci with Memoization and Dynamic Porgramming'''
# def x():

#     # Memoization
#     def fib(n, memo={}):

#         if n in memo:
#             return memo[n]
        
#         if n <= 1:
#             return n
        
#         memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

#         return memo[n]


#     print(fib(10))  # Output: 55


#     # Dynamic Programming
#     def fib(n):

#         if n <= 1:
#             return n
        
#         dp = [0] * (n + 1)
#         dp[1] = 1

#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]

#         return dp[n]

#     print(fib(10))  # Output: 55

'''Levenshtein Distance'''
# def x():
    
#     def minDistance(word1: str, word2: str) -> int:

#         # Capture each word length
#         m, n = len(word1), len(word2)
        
#         # initialize the dp matrix
#         dp = [[0]*(n+1) for _ in range(m+1)]
        
#         # Fill the first column
#         for i in range(1, m+1):
#             dp[i][0] = i
        
#         # fill the first row
#         for j in range(1, n+1):
#             dp[0][j] = j

#         # Populate the rest of the matrix
#         for i in range(1, m+1):
#             for j in range(1, n+1):

#                 if word1[i-1] == word2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]    # No operation needed
                
#                 else:
#                     dp[i][j] = min(
#                         dp[i-1][j-1] + 1,   # Replace Operation
#                         dp[i][j-1] + 1,   # Insert Operation
#                         dp[i-1][j] + 1,   # Delete Operation
#                     )
               
#         # Return the last cell which will contain the minimum number of operations
#         return dp[-1][-1]

'''Function to manage API responses with pagination'''
# def getAverageTemperatureForUser(userId):
    
#     import requests, json

#     base_url = "https://jsonmock.hackerrank.com/api/medical_records"
#     page = 1
#     total_temperatures = []
#     PATH = r'Job Search\HackerRank\Software Developer Certificate\retrived_data.json'

#     dump = {}

#     while True:

#         # Fetch the page data
#         url = f"{base_url}?userId={userId}&page={page}"

#         # Set the GET request
#         response = requests.get(url)

#         # Set the request response
#         data = response.json()
        
#         # Store the retrieved page data in the 'dump' variable
#         dump[f"page {page} response"] = data

#         # Check if there are more pages still
#         if page >= data["total_pages"]:
#             break

#         # Move one page ahead
#         page += 1

#     with open(PATH, 'w') as f:
#         # Dump the JSON data un the JSON file
#             json.dump(dump, f, indent=2)
    
#     return

"""How to store all paths in a BST"""
# def x():

#     # Recursively
#     def find_all_paths(root: Optional[TreeNode]) -> List[List[int]]:
        
#         # Aux Recursive Function Definition
#         def dfs(node: Optional[TreeNode], path: List, all_paths: List) -> None:
            
#             # No node guard
#             if not node:
#                 return None

#             # Append current node value to path
#             path.append(node.val)

#             # If it's a leaf node, save the path
#             if not node.left and not node.right:
#                 all_paths.append(path[:])  # Append a copy of the current path
            
#             # Traverse left and right subtrees
#             dfs(node.left, path, all_paths)
#             dfs(node.right, path, all_paths)

#             # Backtrack: Remove the last node to explore other paths
#             path.pop()
        
#         # Initialize an empty list holder to store the paths
#         result = []

#         # Make the rec. func. call
#         dfs(node=root, path=[], all_paths=result)

#         # Return all the paths traversed
#         return result


#     # Testing
#     root = [1,2,5,3,4,None,6]
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(3)
#     root.left.right = TreeNode(4)
#     root.right.right = TreeNode(6)

#     pretty_print_bst(root)

#     paths = find_all_paths(root=root)

#     print(paths)
#     # Output: [[1, 2, 3], [1, 2, 4], [1, 5, 6]]




#     # Iteratively
#     def find_all_paths(root: Optional[TreeNode]) -> List[List[int]]:
    
#         # No node guard
#         if not root:
#             return None
            
#         # Initialize the stack to hold the running path
#         stack = [(root, [root.val])]

#         # Initialize an empty holder for the paths to be stored
#         all_paths = []

#         # Traverse the tree
#         while stack:

#             # Take the last element in the stack
#             node, path = stack.pop()

#             # If it's a leaf node, save it to the path
#             if not node.left and not node.right:
#                 all_paths.append(path)

#             # Push right and left children onto the stack (copy path for each)
#             if node.right:
#                 stack.append((node.right, path + [node.right.val]))

#             if node.left:
#                 stack.append((node.left, path + [node.left.val]))

#         # Return all the paths traversed
#         return all_paths

#     # Testing
#     root = [1,2,5,3,4,None,6]
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(3)
#     root.left.right = TreeNode(4)
#     root.right.right = TreeNode(6)

#     pretty_print_bst(root)

#     paths = find_all_paths(root=root)

#     print(paths)
#     # Output: [[1, 2, 3], [1, 2, 4], [1, 5, 6]]

"""xxx"""








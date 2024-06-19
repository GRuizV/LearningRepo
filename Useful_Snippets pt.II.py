'''
Snippets Index

- Roman to Integer & Integer to Roman case.
- All permutations from a iterable. (RC)
- Kadane's Algorithm (DS)
- LeetCode Challenge #62. Unique Paths (DS)
- Floyd's Cycle Detection Algorithm (TP)



*RC: Recursion
*DS: Dynamic Programming
*TP: Two-pointers

(5)

'''



"Roman to Integer & Integer to Roman case"

# # Roman to Integer
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



# # Integer to Roman
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





'All permutations from a iterable'

# nums = [1,2,3,4]

# def permutations(nums):

#     if len(nums) == 0:
#         return []
    
#     if len(nums) == 1:
#         return [nums]
    
#     lst = []

#     for i in range(len(nums)):

#         num = nums[i]
#         rest = nums[:i] + nums[i+1:]

#         for perm in permutations(rest):
#             lst.append([num] + perm)

#     return lst

# print(permutations(nums))





"Kadane's Algorithm (Dynamic Programming)"

'''
This algorithm designed by Joseph Kadane solves quite efficiently the problem
of finding a subsegment that fits a max or minimum (or any other criteria for that matter)

'''


# nums = [-2,1,-3,4,-1,2,1,-5,4]
# # Output: 6 / [4,-1,2,1]


# def kadanes(nums):

#     max_ending_here = max_so_far = nums[0]

#     for num in nums[1:]:

#         max_ending_here = max(num, max_ending_here + num)
#         max_so_far = max(max_so_far, max_ending_here)
    
#     return max_so_far

# print(kadanes(nums))    # Output: 6





"1st Dynamic Programming Problem - LeetCode Challenge #62. Unique Paths"

'''
Notes:

The basis of the Dynamic Programming is to "Cache" a solution and store it into a grid to later use it
to save computing resources.

The grid is populated by 1's and summing to the right and down, the bottom right cell will hold the total number of unique ways to get there.

------------------------------------------------------------------------------------

This problem was pretty similar to the one on Turing's tests, althought here is requested
to find a bigger scale of thar problem. The classic 'How many ways would be to get from x to y',

if the problem were only set to m = 2, it'd be solved with fibonacci, but sadly that was not the case,
here, Dynamic Programming was needed.

The problem is graphically explained here: https://www.youtube.com/watch?v=IlEsdxuD4lY

But the actual answer I rather take it from the leetCode's solutions wall, since is more intuitive to me.

'''

# Input

# # Case 1:
# m, n = 3, 7
# # Output: 28

# # Case 2:
# m, n = 3, 2
# # Output: 3


# Solution

# def uniquePaths(m: int, n: int) -> int:

#     # Handling the corner case in which any dimention is 0
#     if n == 0 or m == 0:
#         return 0


#     # Here the grid is initialized
#     result = [[0]*n for _ in range(m)]

#     # The first column of the grid is set to 1, since there is only (1) way to get to each cell of that column
#     for row in range(m):
#         result[row][0] = 1

#     # The first row of the grid is set to 1, since there is only (1) way to get to each cell of that row
#     for col in range(n):
#         result[0][col] = 1


#     # Here all the grid is traversed summing up the cells to the left and up, since are the only ways to get to the current cell
#     # The range starts in 1 since all the first column and row are populated, so the traversing should start in [1,1]
#     for i in range(1, m):

#         for j in range(1, n):

#             result[i][j] = result[i-1][j] + result[i][j-1]
    

#     # The bottom right cell will store all the unique ways to get there
#     return result[-1][-1]


# print(uniquePaths(m, n))





"Floyd's Cycle Detection Algorithm (Two-Pointers)"

'''
also known as the "tortoise and hare" algorithm, is a pointer algorithm that uses two pointers moving at different speeds to detect cycles in a sequence of values.

'''


# nums = [-2,1,-3,4,-1,2,1,-5,4]
# # Output: 6 / [4,-1,2,1]


# def floyd_cycle_detection(sequence):
#     def next_value(x):
#         # This function should return the next value in the sequence.
#         # You need to define this based on your specific problem.
#         pass

#     slow = sequence
#     fast = sequence

#     while True:
#         slow = next_value(slow)
#         fast = next_value(next_value(fast))
        
#         if slow == fast:
#             break

#     # Find the start of the cycle
#     slow = sequence
#     while slow != fast:
#         slow = next_value(slow)
#         fast = next_value(fast)

#     return slow  # This is the start of the cycle





"xxx"











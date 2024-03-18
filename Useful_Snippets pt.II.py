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

# )





"Kadane's Algorithm"

'''
This algorithm designed by Joseph Kadane solves quite efficiently the problem
of finding a subsegment that fits a max or minimum (or any other criteria for that matter)

'''


nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6 / [4,-1,2,1]


def kadanes(nums):

    max_ending_here = max_so_far = nums[0]

    for num in nums[1:]:

        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

print(kadanes(nums))    # Output: 6
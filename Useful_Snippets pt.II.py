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





'3 ways to build the fibonaccis sequence up to a certain number'

# # Input
# s = 10

'function version'
# def fibonacci(n):

#     if not n:
#         return []
    
#     result = [0,1]

#     for i in range(n-2):

#         result.append(result[i]+result[i+1])

#     if n == 1:
#         return result[0]
    
#     return result

# print(fibonacci(s))


'generator version'
# def fibonacci_gen(x=0, y=1):

#     yield x

#     while True:

#         yield y

#         x, y = y, x + y

# gen = fibonacci_gen()
# result = []

# for _ in range(s):

#     result.append(next(gen))

# print(result)



'recursive version'
# def fibonacci(k):

#     def rec_fibonacci(n):
        
#         if n == 0: return 0
#         if n == 1: return 1
        
#         return rec_fibonacci(n-2) + rec_fibonacci(n-1)

#     result = []

#     for i in range(k):
#         result.append(rec_fibonacci(i))

#     return result
   
# print(fibonacci(s))







"xxx"
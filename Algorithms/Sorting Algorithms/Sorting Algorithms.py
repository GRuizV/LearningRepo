import random
import statistics
import timeit



'Bubble Sort'

# setup = '''
# import random
# nums = [random.randint(0,10) for x in range(10)]
# def bubble_sort(lst):

#     swapped = True

#     while swapped is not False:

#         swapped = False
#         i = 0

#         while True:

#             if i == len(lst)-1:
#                 break

#             if lst[i] > lst[i+1]:
                
#                 swapped = True
#                 lst[i], lst[i+1] = lst[i+1], lst[i]

#             i += 1

#     return lst   
# '''


# # Sample Data
# nums = [random.randint(0,10) for x in range(10)]


# def bubble_sort(lst):

#     swapped = True

#     while swapped is not False:

#         swapped = False
#         i = 0

#         while True:

#             if i == len(lst)-1:
#                 break

#             if lst[i] > lst[i+1]:
                
#                 swapped = True
#                 lst[i], lst[i+1] = lst[i+1], lst[i]

#             i += 1

#     return lst     


# # Example usage
# print(nums)
# print(bubble_sort(nums))

# print(f"Bubble Sorting 100k of 10 elements random number lists takes {timeit.timeit('bubble_sort(nums)', setup, number = 100000):.2f}s", end='\n\n')



'Merge Sort'

# setup = '''
# import random
# nums = [random.randint(0,10) for x in range(10)]
# def merge_sort(arr):
    
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)

#     return merge(left_half, right_half)


# def merge(left, right):
    
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
        
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result 
# '''


# # Sample Data
# nums = [random.randint(0,10) for x in range(10)]


# def merge_sort(arr):
    
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)

#     return merge(left_half, right_half)


# def merge(left, right):
    
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
        
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# # Example usage
# print(nums)
# print(merge_sort(nums))
# print(f"Merge Sorting 100k of 10 elements random number lists takes {timeit.timeit('merge_sort(nums)', setup, number = 100000):.2f}s", end='\n\n')




'Quick Sort'

# setup = '''
# import random
# import statistics
# nums = [random.randint(0,10) for x in range(10)]
# def quick_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers
    
#     else:

#         pivot = statistics.median([numbers[0], numbers[len(numbers)//2], numbers[-1]])

#     items_less = [num for num in numbers if num < pivot]
#     pivot_items = [num for num in numbers if num == pivot]
#     items_greater =  [num for num in numbers if num > pivot]


#     return quick_sort(items_less) + pivot_items + quick_sort(items_greater) 
# '''


# # Sample Data
# nums = [random.randint(0,10) for x in range(10)]


# def quick_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers
    
#     else:

#         pivot = statistics.median([numbers[0], numbers[len(numbers)//2], numbers[-1]])

#     items_less = [num for num in numbers if num < pivot]
#     pivot_items = [num for num in numbers if num == pivot]
#     items_greater =  [num for num in numbers if num > pivot]


#     return quick_sort(items_less) + pivot_items + quick_sort(items_greater)


# # Example usage
# print(nums)
# print(quick_sort(nums))
# print(f"Quick Sorting 100k of 10 elements random number lists takes {timeit.timeit('quick_sort(nums)', setup, number = 100000):.2f}s", end='\n\n')



















































import random


'Sorting - Mark and Toys'


# budget = 50

# toys = [1, 12, 5, 111, 200, 1000, 10]
# print(toys)



# # With Bubble Sort was not efficient enough
# swapped = True

# while swapped is True:

#     swapped = False
#     i = 0

#     while True:

#         if i == len(toys)-1:
#             break

#         if toys[i] > toys[i+1]:

#             swapped = True

#             toys[i], toys[i+1] = toys[i+1], toys[i]

#         i += 1



# # Let's try with Merge Sort

# def merge_sort(arr):

#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr)//2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     return merge(left, right)



# def merge(left, right): 

#     result = list()
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


# toys = merge_sort(toys)

# print(toys)


# toys_purchased = list()
# spent = 0

   
# for i in toys:

#     toys_purchased.append(i)

#     spent += i

#     if spent > budget:

#         spent-= i
#         toys_purchased.pop()

#         break
       
        

# print(toys_purchased)



'Sorting - Comparator'

# # At base, the task is to sort descending first by score and ascending by name second

# a = [['amy', 100], ['david', 100], ['heraldo', 75], ['aakansha', 75], ['aleksa', 150]]

# a = sorted(a, key= lambda x: (-x[1], x[0])) # Fundamentally, here's the answer.
# # a = sorted(a, key= lambda x: -x[1])
# # a = sorted(a, key= lambda x: (x[1], x[0]))

# print(a)





'Sorting - Fraudulent Activity Notifications'


# # exp = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# # exp = [1,2,3,4,4]
# exp = [10, 20, 30, 40, 50]

# # d = 5
# # d = 4
# d = 3

' My solution'

# notifications = int()

# exp_base = sorted(exp[:d])

# if d % 2 == 0:
#     median = sum([exp_base[d//2-1], exp_base[d//2]]) / 2

# else:
#     median = exp_base[d//2]


# for i in exp[d:]:
    
#     if i >= 2 * median:
#         notifications += 1


# print(notifications)




"   ChatGPT's solution - Sliding window for meadian algorithm "


# def activity_notifications(expenditure, d):

#     def get_median(count_array, d):

#         if d % 2 == 1:

#             # For odd days, the median is the middle value
#             middle_index = d // 2

#             for i, count in enumerate(count_array):

#                 middle_index -= count

#                 if middle_index < 0:
#                     return i
                
#         else:

#             # For even days, the median is the average of two middle values
#             first_middle = None
#             second_middle = None
#             middle_count = 0

#             for i, count in enumerate(count_array):

#                 middle_count += count

#                 if middle_count >= d // 2 and first_middle is None:
#                     first_middle = i

#                 if middle_count >= d // 2 + 1 and second_middle is None:
#                     second_middle = i                    
#                     break

#             return (first_middle + second_middle) / 2


#     n = len(expenditure)

#     fraud_count = 0

#     # Initialize the count array for the first d days
#     count_array = [0] * 201

#     for i in range(d):
#         count_array[expenditure[i]] += 1


#     for i in range(d, n):
#         median = get_median(count_array, d)
#         if expenditure[i] >= 2 * median:
#             fraud_count += 1
#         print(f'\nmedian: {median}\n')
#         # Update the count array for the sliding window
#         count_array[expenditure[i - d]] -= 1
#         count_array[expenditure[i]] += 1

#     return fraud_count


# res = activity_notifications(exp,d)

# print(res)




'Sorting - Merge Sort: Counting Inversions'

'''
    Notes: after speding considerable time over this, I came to ask for help to chatGPT, and it turned to be a problem
    that could be solved by using a modified version of the Merge Sort algorithm, and what lost me is when the recursion is involved to help the counting,
    this far in my studies I think that I understand the Merge sort basis, but when it comes to recursion I am still not capable to use it to solve problems like this one.

    To my understanding right now, the main modifications done to the algorithm was:

        1. The basic 'Merge Sort' function of the algorithm now not only returns the sorted array, but also keeps the count each time a inversion happens.

        2. In at the end of the recursion, it always merges what is counted in the left side and what is counted on the right side as 'Total count'.
            - From bottom-up after finishing recursively arraging the array, it keeps all the inversions, in the 'total count' made throughout the execution of the sorting function.

        3. in the sorting function, it has a little modification within the While loop, it nows consider being equal or lesser than the right half as not an inversion changing
        from the original " if left[i] < right[j]: result.append(left[i]), i += 1 " to " if left[i] <= right[j]: result.append(left[i]), i += 1 ".
            - That little change makes a huge difference since if the function hits the 'else' part, it will count to the inversions.

        4. the inversion count 'split_inversions += len(left) - i': Seems little confusing at first but it counts correctly since if an element from right is to be added
        to the subarray and there is still element remaining in left, all those elements are inversions done instanly:

        ex:
            let's say: a = [3, 5, 7, 4, 6],

            when the algorithm compares left [3,5,7] and right [4,6], after adding '3', it will add '4', but '4' will have to jump all the way over '5' and '7'
            so the expresion 'split_inversions += len(left) - i' will account for those inversions.


'''


# ChatGPT's solution

# def count_inversions(arr):

#     # Base case: If the array has 0 or 1 elements, it's already sorted with 0 inversions.
#     if len(arr) <= 1:
#         return arr, 0

#     # Split the array into two halves.
#     mid = len(arr) // 2
#     left_half, right_half = arr[:mid], arr[mid:]

#     # Recursive step: Sort and count inversions in the left and right halves.
#     left_half, left_inversions = count_inversions(left_half)
#     right_half, right_inversions = count_inversions(right_half)

#     # Merge the sorted halves while counting split inversions.
#     merged_arr, split_inversions = merge_and_count_split_inversions(left_half, right_half)

#     # Total inversions = left inversions + right inversions + split inversions
#     total_inversions = left_inversions + right_inversions + split_inversions

#     return merged_arr, total_inversions



# def merge_and_count_split_inversions(left, right):

#     merged = []
#     split_inversions = 0
#     i = j = 0

#     while i < len(left) and j < len(right):

#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1

#         else:
#             # If left[i] > right[j], it's an inversion with all elements remaining in the left array.
#             merged.append(right[j])
#             j += 1
#             split_inversions += len(left) - i


#     # Append the remaining elements from both halves (if any).
#     merged.extend(left[i:])
#     merged.extend(right[j:])

#     return merged, split_inversions


# # Example usage:
# arr = [2,1,3,1,2]
# sorted_arr, inversions = count_inversions(arr)

# print("Sorted Array:", sorted_arr)
# print("Inversions:", inversions)






        















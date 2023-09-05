
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





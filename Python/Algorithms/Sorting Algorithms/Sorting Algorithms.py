import random
import statistics
import timeit



'Bubble Sort'

# # Sample Data
# nums = [random.randint(0,10) for x in range(10)]

def bubble_sort(arr):

    swapped = True

    while swapped is not False:

        swapped = False
        i = 0

        while True:

            if i == len(arr)-1:
                break

            if arr[i] > arr[i+1]:
                
                swapped = True
                arr[i], arr[i+1] = arr[i+1], arr[i]

            i += 1

    return arr     


# # Example usage
# print(nums)
# print(bubble_sort(nums))



'Insertion Sort'

# # Sample Data
# nums = [random.randint(0,10) for x in range(5)]

def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i -1

        while j >= 0 and key < arr[j]:

            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

    return arr     


# # Example usage
# print(nums)
# print(insertion_sort(nums))




'Merge Sort'

# # Sample Data
# nums = [random.randint(0,10) for x in range(10)]

def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# # Example usage
# print(nums)
# print(merge_sort(nums))




'Quick Sort'

# # Sample Data
# nums = [random.randint(0,10) for x in range(10)]

def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers
    
    else:

        pivot = statistics.median([numbers[0], numbers[len(numbers)//2], numbers[-1]])

    items_less = [num for num in numbers if num < pivot]
    pivot_items = [num for num in numbers if num == pivot]
    items_greater =  [num for num in numbers if num > pivot]


    return quick_sort(items_less) + pivot_items + quick_sort(items_greater)


# # Example usage
# print(nums)
# print(quick_sort(nums))










'Runtime Measuring Sort Algorithm Function'


# Algorithms Setups

bubble_setup = '''
def bubble_sort(lst):

    swapped = True

    while swapped is not False:

        swapped = False
        i = 0

        while True:

            if i == len(lst)-1:
                break

            if lst[i] > lst[i+1]:
                
                swapped = True
                lst[i], lst[i+1] = lst[i+1], lst[i]

            i += 1

    return lst   
'''

insertion_setup = '''
def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i -1

        while j >= 0 and key < arr[j]:

            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

    return arr 
'''

merge_setup = '''

def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result 
'''

quick_setup = '''
import statistics
def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers
    
    else:

        pivot = statistics.median([numbers[0], numbers[len(numbers)//2], numbers[-1]])

    items_less = [num for num in numbers if num < pivot]
    pivot_items = [num for num in numbers if num == pivot]
    items_greater =  [num for num in numbers if num > pivot]


    return quick_sort(items_less) + pivot_items + quick_sort(items_greater) 
'''

sorted_setup = '''def sorted_al(numbers): return sorted(numbers)'''



# Sample data
ARRAY_LEN = 10
array = [random.randint(0,1000) for _ in range(ARRAY_LEN)]


# The function
def run_sorting_algorithm(algorithm, setup, array):
    
    stmt = f"{algorithm}({array})"

    times = timeit.repeat(setup=setup, stmt=stmt, repeat=3, number=10 )

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times):.2E}s")



# # The execution
# algorithm = 'merge_sort'


# if 'bubble' in algorithm: run_sorting_algorithm(algorithm, bubble_setup, array)
# elif 'quick'in algorithm: run_sorting_algorithm(algorithm, quick_setup, array)
# elif 'merge'in algorithm: run_sorting_algorithm(algorithm, merge_setup, array)
# elif 'sorted'in algorithm: run_sorting_algorithm(algorithm, sorted_setup, array)
# elif 'insertion'in algorithm: run_sorting_algorithm(algorithm, insertion_setup, array)





# # Rankings
# def run_sorting_algorithm(algorithm, setup, array):
    
#     stmt = f"{algorithm}({array})"

#     times = timeit.repeat(setup=setup, stmt=stmt, repeat=3, number=10 )

#     # print(f"Algorithm: {algorithm}. Minimum execution time: {min(times):.2E}s")

#     return algorithm, min(times)


# bubble = run_sorting_algorithm('bubble_sort', bubble_setup, array)
# insertion = run_sorting_algorithm('insertion_sort', insertion_setup, array)
# merge_s = run_sorting_algorithm('merge_sort', merge_setup, array)
# quick = run_sorting_algorithm('quick_sort', quick_setup, array)
# sorted_s = run_sorting_algorithm('sorted', sorted_setup, array)


# results = sorted([bubble, insertion, merge_s, quick, sorted_s], key= lambda x: x[1])
# cent_char = len( max( [x[0] for x in results], key = lambda x: len(x) ))
# pos = 1

# for i in results:    
#     print(f"{pos}. {i[0]:<{cent_char}} {i[1]:.2E}s")
#     pos += 1































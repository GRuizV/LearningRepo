import random
from timeit import default_timer as timer



''' Base sorting algorythm '''


# # Initialize array     
# arr = [ x for x in range(1000,0,-1) ] 

# # Displaying elements of original array    
# # print(f'Elements of the original array: {arr}')    

# s = timer()  

# #Sort the array in ascending order    
# for i in range( len(arr) ): 

#     for j in range( i + 1, len(arr) ): 

#         if(arr[i] > arr[j]):  # '>' will set an asceding order and '<' will set descending 

#             arr[i], arr[j] = arr[j], arr[i]

# e = timer()     

# # Displaying elements of the array after sorting        
# # print(f'Elements of array sorted in ascending order: {arr}', e-s )

# print(e-s)




''' My version of the algorythm without double iteration '''


# arr = [x for x in range(1000,0,-1)] 

# # print(f'Array before sortring {arr}')

# s = timer()  

# for i in range( len(arr) - 1 ):

#     li = arr[ i - len(arr) : ]

#     index = li.index( min( li )) + i  # 'i' must be sum up at the end to compensate that 'li' starts from i - len(arr)

#     if arr[i] > arr[ index ]:  
        
#         arr[i], arr[ index ] = arr[ index ], arr[i]


# e = timer()      

# # print(f'Array after sortring {arr}', e-s)

# print(e-s)
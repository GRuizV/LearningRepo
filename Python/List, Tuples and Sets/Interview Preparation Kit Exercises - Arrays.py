
'Arrays - 2D Arrays - DS'

'Sketching the solution'

# a = '1 1 1 0 0 0 0 1 0 2 3 0 1 1 1 5 4 4'

# a = list(map(int, a.split()))

'''
[1, 1, 1, 0, 0, 0]
[0, 1, 0, 2, 3, 0]
[1, 1, 1, 5, 4, 4]
'''
# a = [x for x in (a[0:6], a[6:12], a[12:])]

# b =  list()

# # Grouping up hourglass items
# for i in range(4):

#     b.append([ a[0][i:i+3], a[1][i+1], a[2][i:i+3] ])

'''
[[1, 1, 1], 1, [1, 1, 1]]
[[1, 1, 0], 0, [1, 1, 5]]
[[1, 0, 0], 2, [1, 5, 4]]
[[0, 0, 0], 3, [5, 4, 4]]
'''
# for i in b: print(i)


# d = list()

# # Summing up elements
# for i in b:

#     d.append( sum(i[0]) + i[1] + sum(i[2])) 


# print(d)


'-----------------------------------------'

'Actual Problem'

# a = '1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0'

# a = list(map(int, a.split()))

# a = [x for x in ( a[0:6], a[6:12], a[12:18], a[18:24], a[24:30], a[30:] ) ]

# '''
# [1, 1, 1, 0, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [1, 1, 1, 0, 0, 0]
# [0, 0, 2, 4, 4, 0]
# [0, 0, 0, 2, 0, 0]
# [0, 0, 1, 2, 4, 0]
# '''
# # for i in a : print(i)

# b = list()

# for i in range(4):

#     for j in range(4):

#         b.append( [ a[i][j:j+3], a[i+1][j+1], a[i+2][j:j+3] ] )    



# '''
# [[1, 1, 1], 1, [1, 1, 1]]
# [[1, 1, 0], 0, [1, 1, 0]]
# [[1, 0, 0], 0, [1, 0, 0]]
# [[0, 0, 0], 0, [0, 0, 0]]
# [[0, 1, 0], 1, [0, 0, 2]]
# [[1, 0, 0], 1, [0, 2, 4]]
# [[0, 0, 0], 0, [2, 4, 4]]
# [[0, 0, 0], 0, [4, 4, 0]]
# [[1, 1, 1], 0, [0, 0, 0]]
# [[1, 1, 0], 2, [0, 0, 2]]
# [[1, 0, 0], 4, [0, 2, 0]]
# [[0, 0, 0], 4, [2, 0, 0]]
# [[0, 0, 2], 0, [0, 0, 1]]
# [[0, 2, 4], 0, [0, 1, 2]]
# [[2, 4, 4], 2, [1, 2, 4]]
# [[4, 4, 0], 0, [2, 4, 0]]
# '''
# # for i in b: print(i)

# c = list()

# for i in range(len(b)):
#     c.append( sum(b[i][0]) + b[i][1] + sum(b[i][2])  )



# res = max(c)

# print(res)




'Arrays - Shelock and Squeares'

# a, b = 17, 24

# rang = range(a,b+1)

# # res = [ x for x in rang if math.sqrt(x) == int(math.sqrt(x)) ]

# # print(res)

# a,b = int(math.sqrt(24)) , int(math.sqrt(49))

# res = [x for x in range(a,b+1) if x**2 in rang]

# print(res)




'Arrays - New Year Chaos'
 
# q = [2,1,5,3,4]

# bribes = 0

# for i in range(len(q)-1,0,-1):

#     if q[i] != i+1:

#         if q[i-1] == i+1:

#             bribes += 1

#             q[i-1], q[i] = q[i], q[i-1]

#         elif q[i-2] == i+1:

#             bribes += 2

#             q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]

#         else:

#             print('Too chaotic')
#             break


# print(bribes)




'Arrays - Minimum Swaps'


# q = [x for x in map(int,'4 3 1 2'.split())]
# swaps = 0

# # [False, False, False, False, False]
# visited = [False]*len(q)

# for i in range(len(q)):

#     if visited[i] is False:

#         a = i
#         b = q[i] - 1
#         l = 1

#         visited[i] = True

#         while b != i:

#             visited[b] = True

#             a = b
#             b = q[b]-1
#             l += 1

#         swaps += l-1

# print(swaps)



'Arrays - Array Manipulation'


# n = 10

# queries = [[1,5,3], [4,8,7], [6,9,1]]

# arr = [[0]*n]

# # print(arr)
# # print()

# for i in range(len(queries)):

#     j = i+1

#     row = arr[i]

#     hi = queries[i][1]+1
#     low = queries[i][0]
#     summand = queries[i][2]

#     row = row[:low-1] + [x + summand for x in row[low-1:hi-1]] + row[hi-1:]

#     arr.append(row)


# for i in arr:
#     print(i)
# print()


# ans = list(map(max,arr))

# print(max(ans))
# print()


#Essentially with this solution the problem is solved, but not scalable, so for hackerrank there has to be a more efficient way to do it in large scale.


'--------------------------------------------------'


# #ChatGPTs & some guy in the discussion section brought a solution base on the concept of 'prefix sums'

# print()
# print('XXXXX Prefix Sums Solution XXXXX')
# print()


# def array_manipulation_2(n, queries):
            
#         ans = [0] * n
        
#         for i in queries:
            
#             a, b, k = i

#             ans[a-1] += k
            
#             if b < len(ans):
                
#                 ans[b] -= k
            
#             print(ans)
                           
                
#         current_sum = 0
#         max_value = 0
        
#         for i in range(len(ans)):
            
#             current_sum += ans[i]
            
#             max_value = max(max_value,current_sum)
            
#         return max_value


# sol = array_manipulation_2(n, queries)


# print()
# print(sol)
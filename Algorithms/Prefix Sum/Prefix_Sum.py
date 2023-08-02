
def prefix_sum(arr):

    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


l = [1,2,3,4,5,6]

res = prefix_sum(l)

print(res)
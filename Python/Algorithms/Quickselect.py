# Code logic: https://youtu.be/XEmy13g1Qxc?si=oytfCBV_f7ObBSzL&t=220

def quick_select(arr, left, right, k):

    def partition(arr, left, right):

        pivot = arr[right]
        i = left

        for j in range(left, right):

            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]

        return i

    def quickselect(arr, left, right, k):

        if left == right:
            return arr[left]

        pivot_index = partition(arr, left, right)

        if k == pivot_index:
            return arr[k]
        
        elif k < pivot_index:
            return quickselect(arr, left, pivot_index - 1, k)
        
        else:
            return quickselect(arr, pivot_index + 1, right, k)

    return quickselect(arr, left, right, k)


# Example usage:
arr = [3, 6, 2, 1, 8, 5, 7]
k = 6
result = quick_select(arr, 0, len(arr) - 1, k)

print(f"The {k+1}-th smallest element is {result}")

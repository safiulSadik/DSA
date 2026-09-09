# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

# What is lower bound?
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

arr = [3,5,8,15,19]
x = 8
ans = len(arr)

def lower_bound(arr, low, high):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans


print(lower_bound(arr, 0, len(arr) - 1))
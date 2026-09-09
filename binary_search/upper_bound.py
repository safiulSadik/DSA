# Implement Upper Bound
# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

# What is Upper Bound?
# The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.
# The upper bound is the smallest index, ind, where arr[ind] > x.

arr = [3,5,8,9,15,19]
x = 9
ans = len(arr)

def upper_bound(arr, low, high):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ans


print(upper_bound(arr, 0, len(arr) - 1))

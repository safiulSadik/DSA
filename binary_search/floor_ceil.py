# Floor and Ceil in Sorted Array

# Problem Statement: ou're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x


arr = [3, 4, 4, 7, 8, 10] 
arr2 = [3, 4, 4, 7, 8, 10] 
x = 8
floor = ceil = len(arr)

def floor_ceil(arr, low, high):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            floor = ceil = arr[mid]
            return floor, ceil

        elif arr[mid] < x:
            floor = arr[mid]
            low = mid + 1
        else:
            ceil = arr[mid]
            high = mid - 1

    return floor, ceil


print(floor_ceil(arr2, 0, len(arr) - 1))
# Last occurrence in a sorted array

# Problem Statement: Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1. Note: Consider 0 based indexing 

target = 13
arr = [3, 4, 13, 13, 13, 20, 40]


def last_occurrence(arr, low, high):
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return ans

print(last_occurrence(arr, 0, len(arr) - 1))


# Count Occurrences in Sorted Array

# Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

x = 2
arr = [2, 2 , 3 , 3 , 3 , 3 , 4]

def find_first(arr, low, high, first):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return first


def find_last(arr, low, high, last):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return last

fst = lst = -1

first = find_first(arr, 0, len(arr) - 1, fst)
last = find_last(arr, 0, len(arr)-1, lst)

if first != -1 and last != -1:
    ans = last - first + 1
else:
    ans = 0

print(ans)
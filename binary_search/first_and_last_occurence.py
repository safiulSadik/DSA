

arr = [3,5,8,8,8,15,19]
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

def upper_bound(arr, low, high):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans - 1

low = lower_bound(arr, 0, len(arr) - 1)
up = upper_bound(arr, 0, len(arr) - 1)

print(low, up)










def find_first(arr, low, high, k, first):
        
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            first = mid
            high = mid - 1

        elif arr[mid] > k:
            high = mid - 1
        
        else:
            low = mid + 1

    return first            


def find_last(arr, low, high, k, last):
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            last = mid
            low = mid + 1
        
        elif arr[mid] > k:
            high = mid - 1

        else:
            low = mid + 1

    return last


first = -1
last = -1

fst = find_first(arr, 0, len(arr)-1, x, first)
lst = find_last(arr, 0, len(arr)-1, x, last)

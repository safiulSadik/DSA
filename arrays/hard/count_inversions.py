
arr = [5,3,2,1,4]
# Result: 7

# Brute Force {
#     Time: O(n^2)
#     Space: O(1)
# }
# cnt = 0

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] > arr[j]:
#             cnt += 1
# print(cnt)



# Optimal (merge sor)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    cnt = 0

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
            cnt += (mid - left + 1)

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    i = 0
    while low <= high:
        arr[low] = temp[i]
        i += 1
        low += 1

    return cnt

def merge_sort(arr, low, high):
    if low >= high:
        return 0

    cnt = 0
    mid = (low + high) // 2

    cnt += merge_sort(arr, low, mid)
    cnt += merge_sort(arr, mid + 1, high)
    cnt += merge(arr, low, mid, high)

    return cnt

print(arr)
print(merge_sort(arr, 0, len(arr) - 1))
print(arr)


arr = [2, 3, 4, 5, 6, 7, 8, 9]

# def search(nums, target):
#         low = 0
#         high = len(nums) - 1

#         while low <= high:
#             mid = (low + high) // 2

#             if nums[mid] == target:
#                 return mid
#             elif target > nums[mid]:
#                 low = mid + 1
#             else:
#                 high = mid - 1
    
#         return -1

def search(arr, low, high, target):
    if low > high:
          return - 1

    mid = (low + high) // 2

    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return search(arr, mid + 1, high, target)
    else:
        return search(arr, low, mid - 1, target)

print(search(arr, 0, len(arr) - 1, 5))   

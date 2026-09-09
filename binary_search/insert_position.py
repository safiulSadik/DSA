
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

nums = [2,4,6,8,9]

ans = len(nums)
low = 0
high = len(nums) - 1
target = 5

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        ans = mid
        break

    elif nums[mid] > target:
        ans = mid
        high = mid - 1

    else:
        low = mid + 1

print(ans)
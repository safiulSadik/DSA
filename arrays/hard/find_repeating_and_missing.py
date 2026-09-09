
# Problem Statement: Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index. 

nums = [1, 2, 3, 6, 7, 5, 7]  
n = len(nums)
# Output: [7, 4] 

# Brute Force {
#   Time: O(n^2)   
#   Space: O(1)
# } 

# ans = [None, None] 

# for i in range(1, len(nums) + 1):
#     cnt = 0

#     for x in nums:
#         if x == i:
#             cnt += 1

#     if cnt > 1:
#         ans[0] = i

#     if cnt == 0:
#         ans[1] = i

# print(ans)




# Better (hashing) {
#     Time: O(2n)
#     Space: O(n)
# }

# freq = {}
# ans = [None, None]

# for num in nums:
#     freq[num] = freq.get(num, 0) + 1

# for i in range(1, len(nums) + 1):
#     if freq.get(i, 0) == 2:
#         ans[0] = i

#     if freq.get(i, 0) == 0:
#         ans[1] = i

# print(ans)




# Optimal (General Math) {
#   Time: O(n)
#   Space: O(1)
# } 

# Sn = (n * (n + 1)) // 2
# S2n = (n * (n + 1) * (2 * n + 1)) // 6
# S = S2 = 0

# for i in range(n):
#     S += nums[i]
#     S2 += nums[i] * nums[i]

# val1 = S - Sn # x - y
# val2 = S2 - S2n  # x^2 - y^2

# # x - y = val1
# # (x + y)(x - y) = val2
# # x + y = val2 / val1
# # x + y + x - y = (val2 / val1) + val1 
# # x = ((val2 / val1) + val1) / 2
# # y = x - val1

# x = ((val2 // val1) + val1) // 2
# y = x - val1

# print(x, y)
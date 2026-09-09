
nums = [4, 2, 2, 6, 4]
k = 6
# Expected: 4

# Brute force {
#     Time: O(n^2)
#     Space: O(1)
# }

# cnt = 0

# for i in range(len(nums)):
#     xor = 0

#     for j in range(i, len(nums)):
#         xor = xor ^ nums[j]

#         if xor == k:
#             cnt += 1

# print(cnt)




# Optimal  

seen = {0: 1}
xr = 0
cnt = 0

for i in range(len(nums)):
    xr = xr ^ nums[i]
    x = xr ^ k

    if x in seen:
        cnt += seen[x]

    seen[xr] = seen.get(xr, 0) + 1

print(cnt)
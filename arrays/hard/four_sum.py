
nums = [1, 0, -1, 0, -2, 2]
target = 0
n = len(nums)
# Expected:
# [[-2, -1, 1, 2],
#  [-2, 0, 0, 2],
#  [-1, 0, 0, 1]]

# Brute force {
#     Time -> O(n^4)
#     Space: O(q) + O(a)
# }
# st = set()
# ans = []

# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             for l in range(k + 1, n):
#                 smm = nums[i] + nums[j] + nums[k] + nums[l]

#                 if smm == target:
#                     temp = [nums[i], nums[j], nums[k], nums[l]]
#                     temp.sort()
#                     st.add(tuple(temp))

# print(st)


# Better solution {
#     Time -> O(n³)
#     Space -> O(n + k) 
# }
# ans = set()

# for i in range(n):
#     for j in range(i + 1, n):
#         hset = set()
#         for k in range(j + 1, n):
#             el4 = - (nums[i] + nums[j] + nums[k])

#             if el4 in hset:
#                 temp = [nums[i], nums[j], nums[k], el4]
#                 temp.sort()
#                 ans.add(tuple(temp))

#             hset.add(nums[k])

# print(ans)




# Optimal {
#     Time: O(n log n + n³)
#     Space: O(1) excluding output, O(k) including output
# }

nums.sort()
n = len(nums)
ans = []

for i in range(n - 3):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    
    for j in range(i + 1, n - 2):
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        k = j + 1
        l = n - 1

        while k < l:
            smm = nums[i] + nums[j] + nums[k] + nums[l]

            if target > smm:
                k += 1
            elif target < smm:
                l -= 1
            else:
                ans.append([nums[i], nums[j], nums[k], nums[l]])

                k += 1
                l -= 1

                while k < l and nums[k] == nums[k - 1]:
                    k += 1
                
                while k < l and nums[l] == nums[l + 1]:
                    l -= 1

print(ans)





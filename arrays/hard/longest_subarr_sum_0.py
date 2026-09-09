
# Brute force {
#     Time: O(n^2)
#     Space: O(1)
# }


# Optimal {
#     Time: O(n) {avg}
#     Space: O(n)
# }

nums = [9, -3, 3, -1, 6, -5]

n = len(nums)
seen = {}
smm = 0
longest = 0

for i in range(n):
    smm += nums[i]

    if smm == 0:
        longest = max(longest, i + 1)

    if smm in seen:
        length = i - seen[smm]
        longest = max(longest, length)

    if smm not in seen:
        seen[smm] = i

print(longest)
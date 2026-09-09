
intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

intervals.sort()
n = len(intervals)
ans = []

# Brute force {
#     Time: O(n log n + n^2)
#     Space: O(n)
# }

# for i in range(n):
#     first = intervals[i][0]
#     second = intervals[i][1]

#     if ans and second <= ans[-1][1]:
#         continue 

#     for j in range(i + 1, n):
#         if intervals[j][0] <= second:
#             second = max(intervals[j][1], second)
#         else:
#             break

#     ans.append([first, second])

# print(ans)

# Optimal {
#     Time: O(n log n + n)
#     Space: O(n)
# }

for i in range(len(intervals)):
    if not ans or ans[-1][1] < intervals[i][0]:
        ans.append(intervals[i])
    else:
        ans[-1][1] = max(ans[-1][1], intervals[i][1])

print(ans)


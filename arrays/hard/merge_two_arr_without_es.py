
# Brute Force {
#     Time: O(2 (n + m))
#     Space: O(n + m)
# }

arr1 = [1, 2, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

n = len(arr1)
m = len(arr2)
i = j = 0

# arr3 = []

# while i < n and j < m:
#     if arr1[i] < arr2[j]:
#         arr3.append(arr1[i])
#         i += 1
#     else:
#         arr3.append(arr2[j])
#         j += 1

# while i < n:
#     arr3.append(arr1[i]) 
#     i += 1

# while j < m:
#     arr3.append(arr2[j]) 
#     j += 1

# for i in range(n):
#     arr1[i] = arr3[i]

# for i in range(n, n + m):
#     arr2[i - n] = arr3[i]

# print(arr3)
# print(arr1)
# print(arr2)




# leetCode

# i = m - 1
# j = n - 1
# k = m + n - 1

# while i >= 0 and j >= 0:
#     if nums1[i] > nums2[j]:
#         nums1[k] = nums1[i]
#         i -= 1
#         k -= 1
#     else:
#         nums1[k] = nums2[j]
#         j -= 1
#         k -= 1
    
# while j >= 0:
#     nums1[k] = nums2[j]
#     j -= 1
#     k -= 1








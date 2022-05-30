nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
# Output: [1]
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
n = 3
m = 3


i = 0
j = 0
sList = []
while j < n:
    sList.append(nums2[j])
    j += 1

while i < m:
    sList.append(nums1[i])
    i += 1
sList = sorted(sList)

# nums1[:] = sList
print(sList)

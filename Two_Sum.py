nums = [3, 2, 4]
target = 6
# [1,2]

result = []
length_of_nums = len(nums)
for i in range(length_of_nums):
    for j in range(i+1, length_of_nums):
        if nums[i] + nums[j] == target:
            result.append(i)
            result.append(j)
print(result)

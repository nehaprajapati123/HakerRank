nums = [0, 1, 0, 3, 12]
# Output: [1,3,12,0,0]

i = 0
while i < len(nums):
    if nums[i] == 0:
        nums.remove(nums[i])
        nums.append(0)
    i = i+1
print(nums)

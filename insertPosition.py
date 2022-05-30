# nums = [1, 3, 5, 6]
# target = 5
# Output: 2

# nums = [1, 3, 5, 6]
# target = 2
# Output: 1

nums = [1, 3, 5, 6]
target = 7
# Output: 4

if target in nums:
    print(nums.index(target))
else:
    if target not in nums:
        nums.append(target)
        nums = (sorted(nums))
        print(nums.index(target))

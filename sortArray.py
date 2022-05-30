# nums = [5,2,3,1]
nums = [5,1,1,2,0,0]

i=0
while i<len(nums):
    j=0
    while j<len(nums):
        if nums[i]<nums[j]:
            a=nums[i]
            nums[i]=nums[j]
            nums[j]=a
        j=j+1
    i=i+1
print(nums)

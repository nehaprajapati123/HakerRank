# nums = [3,1,2,4]
# first even will come hen odd in a list


nums=[0]
num=[]
i=0
while i<len(nums):
    if nums[i]%2==0:
        num.append(nums[i])
    i=i+1
j=0
while j<len(nums):
    if nums[j] not in num:
       num.append( nums[j])
    j=j+1
print(num)


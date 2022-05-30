nums = [2,2,1]
nums = [4,1,2,1,2]
for i in nums:
    c=0
    for j in nums:
        if i==j:
            c=c+1
    if c == 1:
        print(i)
        
        
        
for i in nums:
    if nums.count(i) == 1:
        print( i)
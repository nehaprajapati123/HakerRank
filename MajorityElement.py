from itertools import count


nums = [3,2,3]
nums = [2,2,1,1,1,2,2]

# non_duplicate = list(set(nums))
# for i in non_duplicate:
#     if nums.count(i) > (len(nums)/2):
#         print(i)
        
        
# dic ={}
# for i in nums:
#    c=( nums.count(i))
#    dic[i] = c
# print(dic)
# a =0
# for i in dic:
#     if dic[i] > a:
#         a = dic[i]
#         b = i
# print(b)


# a = 0
# for i in nums:
#     count = nums.count(i)
#     if count>a:
#         a = count
#         b = i
# print(b)


# return max(nums,key=nums.count) 


# n = []                  #To store count of each elements
# for x in nums:
#     count = 0
#     for i in range(len(nums)):
#         if x == nums[i]:
#             count+=1
#     n.append(count)
# a = max(n)              #largest in counts list
# for i in range(len(n)):
#     if n[i] == a:
#         print(nums[i],a)    

nondup_lis=list(set(nums))
for i in nondup_lis:
    if nums.count(i) > (len(nums)/2):
        print(i)
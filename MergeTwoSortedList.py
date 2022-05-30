list1 = [1, 2, 4]
list2 = [1, 3, 4]
# [1,1,2,3,4,4]

# list1.extend(list2)
# for i in list1:
#     a = 0
#     for j in list1:
#         if list1[i] < list1[j]:
#             a = list1[i]
#             list1[i] = list1[j]
#             list1[j] = a
# print(list1)


i = 0
while i < len(list1):
    list2.append(list1[i])
    i = i+1
print(sorted(list2))

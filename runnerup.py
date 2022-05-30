arr = [4, 5, 3, 7, 54, 6]
# maxnum = max(arr)
# c = arr.count(maxnum)
# for i in range(c):
#     arr.remove(maxnum)
# print(max(arr))


b = set(arr)
b.remove(max(b))
print(max(b))

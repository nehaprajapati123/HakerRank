array = [1, 2, 3, 4, 5, 6, 7]
k = 2
for i in range(k):
    a = array.pop()
    array.insert(0, a)
print(array)


i = 0
while i < k:
    a = array.pop()
    array.insert(0, a)
    i = i+1
print(array)

limit = int(input())
arr = list(map(int,input().split()))
count0 = arr.count(0)
count1 = arr.count(1)
if count0 < count1:
    print(count0*2)
else:
    print(count1*2)
# print(count0)
# print(count1)
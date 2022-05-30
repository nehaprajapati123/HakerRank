T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    a = set()
    for i in range(1,N):
        if arr[i-1] != arr[i]:
            a.add(i-1)
            a.add(i)
    print(len(a))
    print(a)

# a = [1,2,3,3,4]
# b=set()
# for i in a:
#     b.add()
# print(b)
    
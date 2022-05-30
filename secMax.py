limit = int(input())
arr = list(map(int,input().split()))

if len(arr)>1:
    arr = sorted(arr)
    arr.remove(arr[-1])
    print(arr[-1])
    
else:
    print(-1)
    
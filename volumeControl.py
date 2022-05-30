T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    if Y-X >0:
        print(Y -X)
    else:
        print(X-Y)
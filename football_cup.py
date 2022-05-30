T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    if X >0 and Y>0:
        if X == Y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
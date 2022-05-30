T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    if X>Y:
        print("second")
    elif Y>X:
        print("first")
    else:
        print("any")
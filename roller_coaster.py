T = int(input())
for _ in range(T):
    X,H = map(int,input().split())
    if X >= H:
        print('Yes')
    else:
        print("No")
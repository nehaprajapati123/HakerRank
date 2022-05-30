from sqlalchemy import true


T = int(input())
for _ in range(T):
    N,K,X,Y = map(int,input().split())
    a = []
    while true:
        if X not in a:
            a.append(X)
            if X == Y:
                print("YES")
                break
            X = X+K%N
        else:
            print("NO")
            break
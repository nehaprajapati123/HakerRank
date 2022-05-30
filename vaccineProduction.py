from sqlalchemy import true


D1,V1,D2,V2,P = map(int,input().split())
sum = 0
i = 0
while sum < P:
    if i >= D1:
        sum = sum + V1
    if i >= D2:
        sum = sum + V2
    if sum >= P:
        print(i)
        break
    i = i + 1
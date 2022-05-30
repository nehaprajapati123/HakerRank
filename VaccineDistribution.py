T = int(input())
for _ in range(T):
    N, D = map(int,input().split())
    a = list(map(int,input().split()))
    Risky = 0
    for i in a:
        if (80<=i) or (i<=9):
            Risky +=1
    notRisky = N - Risky
    day1 = 0
    day2 = 0
    if (notRisky % D)==0:
        day1 =(notRisky//D)
    else:
        day1 = (notRisky//D)+1
    if (Risky % D)==0:
        day2 = (Risky//D)
    else:
        day2 = (Risky//D)+1
    days = day1+day2
    print(days)
        

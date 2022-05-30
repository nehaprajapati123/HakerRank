T = int(input("enetr T "))
if 1 <= T <= 10:
    for i in range(T):
        N = int(input("enter length "))
        A = list(map(int,input().split()))
        if len(A) == N:
            if (sum(A)) % 2 == 0:
                print('0')
            elif 2 in A:
                print(1)
            else:
                print(-1)
            
            
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    if len(A) == N:  
        A = set(A)     
        if 0 in A:
            print(len(A)-1)
        else:
            print(len(A))
            
    


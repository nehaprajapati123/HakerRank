T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A= list(map(int,input().split()))
    dup_lis = set(A)
    print(A)
    print(dup_lis)
    i=0
    dic={}
    while i<len(A):
        if A[i] not in dic:
            count = A.count(A[i])
            if count >= K:
                dic[A[i]] = count
            print(dic)

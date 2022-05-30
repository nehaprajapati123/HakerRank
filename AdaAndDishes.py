T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int,input().split()))
    Burner1 = 0
    Burner2 = 0
    length=len(C)
    for i in range(length):
        a = max(C)
        if Burner1 >= Burner2:
            Burner2 += a
            C.remove(a)
        else:
            Burner1 += a
            C.remove(a)
    if Burner1 > Burner2:
        print(Burner1)
    else:
        print(Burner2)
        
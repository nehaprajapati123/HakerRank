T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    
    if ((6//2)*X) < ((6//3)*Y):
        print(((6//2)*X))
        
    elif ((6//2)*X) > ((6//3)*Y):
        print(((6//3)*Y))
        
    else:
        print(((6//2)*X))
        
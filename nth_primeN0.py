limit = int(input())
i=1
c=0
while True:
    j = 1
    k=0
    while j<=i:
    
        if i%j==0:
            k=k+1
        j=j+1
    if k==2:
        c=c+1
        if limit == c:
            print(i)
            break
    i=i+1
         
        
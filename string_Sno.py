a=input("Enter your name ")
i=0
while i<len(a):
    b=(ord(a[i]))
    j=97
    c=0
    while j<=b:
        c=c+1
        j=j+1
    print(a[i]," :- ",c)
    i=i+1
t = int(input("enter the times"))
# for _ in range(t):
a,b = map(int,input("enter the a and b").split())
aeven = a//2
aodd = a - aeven
beven = b//2
bodd = b-beven
ans = (aeven*beven)+(aodd*bodd)
print(ans)
                    
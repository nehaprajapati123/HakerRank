T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input().lower())
    lenOfS  = len(S)
    if lenOfS%2==1:
        lenOfS -= 1
    for i in range(0,lenOfS,2):
        S[i],S[i+1]=S[i+1],S[i]
    # print(S)
    chr = "abcdefghijklmnopqrstuvwxyz"
    str = ""
    for i in S:
        if i in chr:
            index = chr.index(i)
            str += (chr[-(index+1)])
    print(str)
        


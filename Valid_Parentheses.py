# Input: s = "()[]{}"
# Output: true


s = input("enter your Valid Paranthese ")
lis = []
for i in s:
    lis.append(i)
    if len(lis) >= 2:
        if lis[-2]+lis[-1] in ["()", "[]", "{}"]:
            lis.pop()
            lis.pop()
print(len(lis) == 0)

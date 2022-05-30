p = [1, 2, 3]
q = [1, 2, 3]
# Output: true
c = 0
i = 0
while i < len(p):
    if p[i] == q[i]:
        c = c+1
    i = i+1
if c == len(p):
    print(True)
else:
    print(False)

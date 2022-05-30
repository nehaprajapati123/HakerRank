num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
sum = 0
for i in (num1):
    if i not in num2:
        sum+=i
for j in (num2):
    if j not in num1:
        sum+=j
print(sum)
        
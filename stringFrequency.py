from ast import Str


str1 = input()
str1 = sorted(list(str1))
print(str1)
str2 = ""
count =0
for i in str1:
    if i not in str2:
        str2+=i
        count = str1.count(i)
        a=str(count)
        str2 +=a
    
print(str2)
    
    

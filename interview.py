str = input()
list = []
str1 = ""
for i in str:
    if i == "a"  or i == "o" or i == "e" or i == "i" or i == "u":
        list.append(i)
    else:
        str1+=i
print(len(list))
print(str1)
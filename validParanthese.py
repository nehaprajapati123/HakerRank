s = "0P"
# s = "A man, a plan, a canal: Panama"
s = s.lower().replace(" ","")
str = ""
for i in s:
    if i>="a" and i<="z" or i>="0" and i<="9":
        str = str+i
print(str)
if str == str[::-1]:
    print( True)
else:
    print( False)
from re import L
from unicodedata import digit


digits = [9]
#  9+1 = 10 Output: [1,0]
digits = [4, 3, 2, 1]
# Output: [4,3,2,2]

digits = [1, 2, 3]
# Output: [1,2,4]


digits = [9, 9]
# [1,0,0]

# sum = digits[-1] + 1
# sumStr = str(sum)
# digits.remove(digits[-1])
# i = 0
# while i < len(sumStr):
#     num = int(sumStr[i])
#     digits.append(num)
#     i += 1
# print(digits)

str1 = ""
i = 0
while i < len(digits):
    numStr = str(digits[i])
    str1 += numStr
    i = i + 1
num = int(str1) + 1
numStr = str(num)
lis = []
j = 0
while j < len(numStr):
    num = int(numStr[j])
    lis.append(num)
    j = j+1
print(lis)

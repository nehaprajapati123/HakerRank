s = "anagram"
t = "nagaram"
# Output: true

# i = 0
# c = 0
# while i < len(s):
#     if s[i] in t:
#         c = c+1
#     else:
#         pass
#     i = i+1
# if c == len(s):
#     print("true")
# else:
#     print("false")


def fun():
    str1 = input("enter your first word ")
    str2 = input("enter your second word ")

    # i = 0
    # c = 0
    # while i < len(str1):
    #     if str1[i] in str2:
    #         c = c+1
    #     i = i+1
    # if c == len(str2) and c == len(str1):
    #     print("YES")
    # else:
    #     print("NO")
    str1 = sorted(str1)
    str2 = sorted(str2)
    print(len(str1) == len(str2))


fun()

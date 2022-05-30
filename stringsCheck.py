s1 = "bank"
s2 = "kanb"

# s1 = "attack"
# s2 = "defend"

# s1 = "kelb"
# s2 = "kelb"

# c = 0
# i = 0
# while i < len(s1):
#     if s1[i] in s2:
#         c += 1
#     i += 1
# if c == len(s2):
#     print(True)
# else:
#     print(False)


first = []
second = []

for i in range(len(s1)):
    if s1[i] != s2[i]:
        first.insert(0, s1[i])
        second.append(s2[i])

print(s1 == s2 or len(first) == 2 and first == second)

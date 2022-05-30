# list1=[1,2,3]
# list2=[1,2,3]
# print(list1 is list2 )
# list1=list2
# print(list1 is list2 )


# print('abcd@123$'.isalnum())

# print('abcd123'.isalnum())
# print('      Python.lstrip')

# list2=[4,2,3]
# list1.append(5)
# print(list1)
# list1.extend(5)
# print(list1)


# def addToList(val, list=[]):

#  list.append(val)

#  return list

# list1 = addToList(1)

# list2 = addToList(123,[])

# list3 = addToList('a')

# print ("list1 = %s" % list1)

# print ("list2 = %s" % list2)

# print ("list3 = %s" % list3)

# list2=[4,2,3]
# list2[0]=6
# print(list2)
# lis1=(1,2,3)
# lis1[0]=7
# print(lis1)


# print("hii",end=" ")
# print("neha")
# print("neha")


# arbitary argument
# def fun1(*elem):
#     i=0
#     while i<len(elem):
#         print(elem[i])
#         i=i+1
# fun1("neha","satyam")


# arbitary keyword argument
# def fun1(**elem):
#     i=0
#     while i<len(elem):
#         print(i)
#         i=i+1
# fun1(a="neha",b="satyam")


# print(__name__)
# n = int(input("num "))
# div = int(input("div "))

# sum = 0
# i = 0
# while i < n:
#     rem = i % 4
#     sum = sum+rem
#     i = i+1
# print(sum)


# list = [1, 2, 3, 4, 5, 6, 7, 8]

# max = (max(list))
# min = (min(list))
# print(max+min)


from operator import index


k = int(input("enter k no. "))
n = int(input("enter your list len "))
l = []

for i in range(0, n):
    p = int(input("enter your number "))
    l.append(p)


def SumOfNumbers(l, n, k):
    l = sorted(l)
    min = l[k-1]
    max = l[-k]
    return min+max


result = SumOfNumbers(l, n, k)
print(result)

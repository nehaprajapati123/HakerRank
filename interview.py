# a="neha"
# b="prajapati"
# c=" "
# print(a+c+c+c+c+b)

# n=int(input("enter your number"))
# m=int(input("enetr your number"))
# o=int(input("enter your number"))
# if n>m and n>o:
#     if m>o:
#         print(m,"second max")
#     else:
#         print(o,"second max")
# elif m>n and m>o:
#     if n>o:
#         print(n,"second max")
#     else:
#         print(o,"second max")
# elif o>m and o>n:
#     if m>n:
#         print(m,"second max")
#     else:
#         print(n,"second max")
# else:
#     print("something want wrong")


# n=int(input("enetr your number"))
# num=n
# sum=0
# while n>0:
#     rem=n%10
#     j=1
#     c=1
#     while j<=rem:
#         c=c*j
#         j=j+1
#     n=n//10
#     sum=sum+c
# if sum==num:
#     print(num,"strong number")
# else:
#     print(num,"not a strong number")


# a="gulnaaznazrin"
# dic={}
# for i in a:
#     c=1
#     for j in a:
#         if i==j:
#             dic[i]=c
#             c=c+1
# print(dic)

# list2=[]
# n=int(input("enter your number"))


# i=0
# list2=[]
# while i<=n:
#     list1=[]
#     j=0
#     while j<=i:
#         list1.append(j)
#         j=j+1
#     i=i+1
#     list2.append(list1)
# print(list2)

def fun1():
    print(fun2())
def fun2():
    i=1
    while i<=100:
        if i%7==0:
            return i
            
        else:
            pass
        i=i+1
fun1()




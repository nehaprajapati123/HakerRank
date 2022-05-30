def fun():
    str1 = input()    
    str2 = input()
    a,b = sorted(str1),sorted(str2)
    if a == b:
        print("Yes")
    else:
        print("No")
fun()
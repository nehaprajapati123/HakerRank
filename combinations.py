x = int(input("enetr firdt number:  "))
y = int(input("enetr firdt number:  "))
z = int(input("enetr firdt number:  "))
n = int(input("enetr firdt number:  "))
                                                                    
list=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k!=n):
                list.append([i,j,k])
print(list)
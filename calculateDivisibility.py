def fun():
    initial = int(input("initialise "))
    limit = int(input("limit "))
    i = initial
    sum = 0
    while i <= limit:
        if i % 3 == 0 and i % 5 == 0:
            sum = sum + i
        i = i+1
    print(sum)


fun()

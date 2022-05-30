def differenceofSum(n, m):
    for i in range(1, m+1):
        sum1 = 0
        sum2 = 0
        if n % i == 0:
            sum1 += i
        else:
            sum2 += i
    print(sum1)
    print(sum2)
    # if sum1 < sum2:
    #     print(sum2-sum1)
    # else:
    #     print(sum1-sum2
    #           )


n = int(input("number "))
m = int(input("your limit "))

differenceofSum(n, m)

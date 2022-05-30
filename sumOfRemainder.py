n = int(input())
div = int(input())


def FindSumOfRemainders(n, div):
  # write your code here

    sum = 0
    i = 1
    while i <= n:
        rem = i % div
        sum = sum+rem
        i = i+1
    return sum


result = FindSumOfRemainders(n, div)
print(result)

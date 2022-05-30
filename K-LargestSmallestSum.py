k = int(input())
n = int(input())
l = []

for i in range(0, n):
    p = int(input())
    l.append(p)


def SumOfNumbers(l, n, k):
  # write your code here
    l = sorted(l)
    min = l[k-1]
    max = l[-k]
    return min+max


result = SumOfNumbers(l, n, k)
print(result)

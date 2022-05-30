def task(r, unit, arr):
    n = len(arr)
    # We calculate the total amount of food that the rats can consume
    food = r * unit
    sum_arr = 0
    # We calculate the total amount in the households
    for i in arr:
        sum_arr = sum_arr + i
    if len(arr) == 0:
        print(-1)
    elif food > sum_arr:
        print(0)
    # Where 1 represents that the household has surplus food for the rats
    elif food < sum_arr:
        print(1)


task(7, 2, [2, 8, 3, 5, 7, 4, 1, 2])
1


from operator import indexOf


r = int(input())
unit  = int(input())
food = r * unit
n = int(input())
arr = list(map(int,input().split()))
sum = 0
for i in arr:
    if sum < food:
        sum = sum + i
    else:
        print(arr.index(i))
        break
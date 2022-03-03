# BOJ 2480

dice = list(map(int, input().split()))
resultSet = set(dice)

if len(resultSet) == 1:
    print(10000 + 1000 * resultSet.pop())
elif len(resultSet) == 2:
    print(1000 + 100 * sorted(dice)[1])
else:
    print(100 * max(dice))

# BOJ 1463

n = int(input())
memoization = [0, 0, 1, 1]
if n > 3:
    memoization += [0] * (n-3)

def expand(num):

    # operation 3
    ans = memoization[num-1] + 1

    # operation 1
    if num % 2 == 0:
        ans = min(ans, memoization[num // 2] + 1)

    # operation 2
    if num % 3 == 0:
        ans = min(ans, memoization[num // 3] + 1)

    memoization[num] = ans


for i in range(4, n+1):
    expand(i)

print(memoization[n])
# BOJ 2579

# 각 계단의 점수를 s(n), n층까지 올라가며 얻는 총 점수의 최대값을 t(n)
# t(n) = s(n) + max(t(n-2), t(n-3) + s(n-1))

import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]
totals = [0] * n

# except: n < 3
if n < 3:
    print(sum(scores))
    sys.exit()

# base case
totals[0] = scores[0]
totals[1] = scores[0] + scores[1]
totals[2] = max(scores[0], scores[1]) + scores[2]

for i in range(3, n):
    totals[i] = scores[i] + max(totals[i-2], totals[i-3] + scores[i-1])

print(totals[n-1])
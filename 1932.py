# BOJ 1932

import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

table = triangle.copy()

for i in range(1, n):
    for j in range(i+1):
        if 0 < j < i:
            prev = max(table[i-1][j-1], table[i-1][j])
        elif j == 0:
            prev = table[i-1][0]
        elif j == i:
            prev = table[i-1][j-1]

        table[i][j] = prev + table[i][j]

print(max(table[-1]))
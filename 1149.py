# BOJ 1149

# cost[i][color] = i번째 집을 color로 칠하는데 드는 비용
# costAccumulated[i][color] = i번째 집을 color로 칠할 때 1~i까지 색칠하는데 든 최소 비용.
# costAccumulated[i]['r'] = min(costAccumulated[i-1]['g'], costAccumulated[i-1]['b']) + cost[i]['r']
# 다른 색깔도 마찬가지. 즉 시작을 3가지 경우로 나누어 DP를 진행해야 함.

import sys
input = sys.stdin.readline

# Input
N = int(input())
cost = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

# base case
costAccumulated = [[0, 0, 0], cost[1]] + [[0, 0, 0] for _ in range(N-1)]

# DP
for i in range(2, N+1):
    costAccumulated[i][0] = min(costAccumulated[i-1][1], costAccumulated[i-1][2]) + cost[i][0]
    costAccumulated[i][1] = min(costAccumulated[i-1][2], costAccumulated[i-1][0]) + cost[i][1]
    costAccumulated[i][2] = min(costAccumulated[i-1][0], costAccumulated[i-1][1]) + cost[i][2]

print(min(costAccumulated[N]))
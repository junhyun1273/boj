# BOJ 14889
# reference: https://donghak-dev.tistory.com/93

import sys
input = sys.stdin.readline

minAns = float('inf')

def computeStatDiff(team1):
    team2 = [i for i in range(N) if i not in team1]
    team1Sum = sum([stat[i][j] for i in team1 for j in team1])
    team2Sum = sum([stat[i][j] for i in team2 for j in team2])
    return abs(team1Sum - team2Sum)


def dfs(team1, step):

    global minAns

    # base case
    if len(team1) == N // 2:
        minAns = min(minAns, computeStatDiff(team1))
        return

    # Recursive step
    for i in range(step, N):
        if i not in team1:
            # i 다음 수부터 탐색함에 주의 (아니면 시간 초과됨)
            dfs(team1 + [i], i+1)



if __name__ == '__main__':

    # Get input
    N = int(input())
    stat = [list(map(int, input().split())) for _ in range(N)]
    
    assert N % 2 == 0
    for i in range(N):
        assert stat[i][i] == 0
    
    dfs([], 0)

    print(minAns)


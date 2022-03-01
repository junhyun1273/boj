# BOJ 9663
# Python3로는 시간초과됨. pypy3로 실행해야 통과 가능.

N = int(input())
cnt = 0

# 각 row별 퀸이 존재하는 col의 번호
board = [0] * N

# row행에 배치한 퀸이 가능한 케이스인지(서로를 공격하지 않는지) 확인함.
def isPossible(row):
    for i in range(row):
        if board[row] == board[i] or abs(board[row] - board[i]) == abs(row - i):
            return False
    return True

# 주어진 row행에 대해 열을 반복하며 dfs 수행.
def dfs(row):
    global cnt
    for col in range(N):
        board[row] = col
        if isPossible(row):
            if row + 1 == N:
                cnt += 1
            else:
                dfs(row+1)
            
dfs(0)
print(cnt)



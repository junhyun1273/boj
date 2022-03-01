# BOJ 2580

import sys
input = sys.stdin.readline

SIZE = 9
board = [0] * SIZE

for i in range(SIZE):
    row = list(map(int, input().split()))
    board[i] = row

print(board)
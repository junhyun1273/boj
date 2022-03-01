# BOJ 2580

import sys
input = sys.stdin.readline

SIZE = 9
board = [0] * SIZE
emptyPlaceList = []

# Return a set of candidate numbers
# for the given (i, j) index at board
def findCandidates(i, j):
    candidates = set(range(1, 10))

    # 가로 세로로 중복되는 숫자 제거
    for k in range(SIZE):
        c1 = board[i][k]
        c2 = board[k][j]
        if c1 in candidates:
            candidates.remove(c1)
        if c2 in candidates:
            candidates.remove(c2)
    
    # 3x3 정사각형 내에서 중복되는 숫자 제거
    # m, n은 (i,j)가 속한 3x3 정사각형의 시작 인덱스
    m, n = i - i % 3, j - j % 3
    for row in range(m, m+3):
        for col in range(n, n+3):
            c = board[row][col]
            if c in candidates:
                candidates.remove(c)
    
    return candidates

# emptyPlaceList[emptyIndex]에 해당하는 위치에
# 가능한 candidate number를 찾아 dfs로 탐색.
def fillCandidatesRecursive(emptyIndex):

    # 끝까지 탐색한 경우
    if emptyIndex >= len(emptyPlaceList):
        # Print the result out.
        for row in range(SIZE):
            print(*board[row])
        # 여러개 출력하면 안되니 프로세스 종료.
        sys.exit()
    
    i, j = emptyPlaceList[emptyIndex]
    candidates = findCandidates(i, j)

    for c in candidates:
        board[i][j] = c
        fillCandidatesRecursive(emptyIndex + 1)
        board[i][j] = 0

    return


if __name__ == '__main__':

    # Take the sudoku input and store into BOARD.
    # Find the empty places from the given sudoku.
    for i in range(SIZE):
        row = list(map(int, input().split()))
        board[i] = row
        for j in range(SIZE):
            if row[j] == 0:
                emptyPlaceList.append((i, j))

    # Fill the BOARD recursively.
    if len(emptyPlaceList) > 0:
        fillCandidatesRecursive(0)

# BOJ 9184

# Given recursive function w(a, b, c)
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    elif a < b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


import sys

input = sys.stdin.readline
queryList = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        queryList.append((a,b,c))

sheet = [[[1, ] * 21 for _ in range(21)] for _ in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            
            if i < j < k:
                sheet[i][j][k] = sheet[i][j][k-1] + sheet[i][j-1][k-1] - sheet[i][j-1][k]
            
            else:
                sheet[i][j][k] = sheet[i-1][j][k] + sheet[i-1][j-1][k] + sheet[i-1][j][k-1] - sheet[i-1][j-1][k-1]

def answer(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return sheet(20, 20, 20)

    else:
        return sheet(a, b, c)

for (a, b, c) in queryList:
    print(a, b, c, answer(a, b, c))
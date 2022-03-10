# BOJ 10844

n = int(input())

# base case (n = 1)
# 일의 자리수 별로 n자리 계단수의 개수를 dict으로 저장하자
memo = {i:1 for i in range(1, 10)}

for _ in range(n-1):
    
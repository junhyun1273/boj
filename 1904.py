# BOJ 1904

# f(n)을 길이 n인 수열의 개수라 했을 때
# f(n) = f(n-1) + f(n-2)

n = int(input())

# base case: f(1) = 1, f(2) = 2
fibo = [0, 1, 2] + [0] * (n-2)

# DP: (*) 값이 매우 커서 (int형 초과) 메모리 초과되니 15746으로 나눈 값들을 저장
for i in range(3, n+1):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 15746

print(fibo[n])
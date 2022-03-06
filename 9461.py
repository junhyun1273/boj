# BOJ 9461
# Padovan sequence

# Note P(n) = P(n-1) + P(n-5)

import sys
input = sys.stdin.readline

T = int(input())
tests = [int(input()) for _ in range(T)]
maxTest = max(tests)

# base case
sequence = [0, 1, 1, 1, 2, 2]

# DP
for i in range(6, maxTest+1):
    next = sequence[i-1] + sequence[i-5]
    sequence.append(next)

# Print result
print(*[sequence[i] for i in tests], sep='\n')
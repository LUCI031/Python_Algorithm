import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+5)]

dp[1] = 1
dp[2] = 1

for i in range(3,N+1):
    dp[i] = dp[i-2]+dp[i-1]

print(dp[N])

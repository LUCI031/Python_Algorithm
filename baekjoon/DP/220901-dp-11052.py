import sys
input = sys.stdin.readline

N = int(input())

nums = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i],dp[i-k]+nums[k])
    
print(dp[-1])
import sys
input=sys.stdin.readline

N = int(input())
dp = [0]*N
lst = list(map(int, input().split()))
dp[0] = lst[0]
for i in range(N):
    dp[i] = max(lst[i],dp[i-1]+lst[i]) 
    
print(max(dp))



# 시간 초과
# for i in range(N):
#     dp[i] = sum(lst[:i+1])
#     for j in range(i):
#         if sum(lst[j:i+1]) > dp[i]:
#             dp[i] = sum(lst[j:i+1])
    
# print(max(dp))
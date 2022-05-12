# https://www.acmicpc.net/board/view/60664
import sys
input=sys.stdin.readline

lst = [0]
N = int(input())
for i in range(N):
    lst.append(int(input()))
    
dp = [0]
dp.append(lst[1])

if N > 1:
    dp.append(lst[1]+lst[2])
    
for i in range(3,N+1):
    dp.append(max(dp[i-2]+lst[i],dp[i-3]+lst[i-1]+lst[i],dp[i-1]))
    
print(dp[N])
# N = int(input())
# lst = [0]

# for i in range(N):
#     lst.append(int(input()))

# if N < 3:
#     print(sum(lst))
    
# else:
#     dp = [0]*(N+1)
#     dp[1] = lst[1]
#     dp[2] = lst[1]+lst[2]

#     for j in range(3,N+1):
#         dp[j] = (max(dp[j-2]+lst[j],dp[j-3]+lst[j-1]+lst[j]))
#     print(max(dp))
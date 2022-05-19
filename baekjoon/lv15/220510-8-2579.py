# https://sungmin-joo.tistory.com/18

import sys
input=sys.stdin.readline

N = int(input())
lst = [0]

for i in range(N):
    lst.append(int(input()))

if N == 1:
    print(lst[1])

else:
    dp = [0]*(N+1)
    dp[1] = lst[1]
    dp[2] = lst[1]+lst[2]
    
    for j in range(3,N+1):
        dp[j] = (max(dp[j-2]+lst[j],dp[j-3]+lst[j]+lst[j-1]))
    print(dp[N])
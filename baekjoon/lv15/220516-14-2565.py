import sys
input=sys.stdin.readline

N = int(input())
dp = [1] * N 
lst = []

for i in range(N):
    lst.append(list(map(int,input().split())))

lst.sort()    

for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1] and dp[i]<dp[j]+1:
            dp[i] = dp[j]+1
            
print(N-max(dp))
            
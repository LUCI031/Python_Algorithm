# https://kbwplace.tistory.com/77
# 문제 풀이 보고 깨달음 얻어서 품

import sys
input=sys.stdin.readline

peeps = []
ans = []
N = int(input())

for i in range(N):
    peeps.append(list(map(int,input().split())))
    ans.append(1)
    
for j in range(N):
    for k in range(N): 
        if peeps[j][0] < peeps[k][0] and peeps[j][1] < peeps[k][1]:
            ans[j] += 1
            
print(*ans, sep=' ')
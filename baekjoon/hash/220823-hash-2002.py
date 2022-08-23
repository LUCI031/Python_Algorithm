import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dics = defaultdict(int)
lst = []
cnt = 0
for i in range(N):
    dics[input().strip()] = i

for i in range(N):
    lst.append(input().strip())

for i in range(N-1):
    for j in range(i+1,N):
        if dics[lst[i]] > dics[lst[j]]:
            cnt += 1
            break

print(cnt)
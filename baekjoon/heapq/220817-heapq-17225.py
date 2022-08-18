import sys
import heapq as h
input = sys.stdin.readline

A,B,N = map(int,input().split())
start = 0
s_end = 0
j_end = 0
sangmin = []
jisu = []
lst = []

for _ in range(N):
    T,C,M = map(str,input().split())
    T = int(T)
    M = int(M)
    if C == 'B':
        start = max(T,s_end)
        for j in range(M):
            h.heappush(lst,[start, 'B'])
            start += A
            s_end = start
    else:
        start = max(T,j_end)

        for j in range(M):
            h.heappush(lst,[start, 'R'])
            start += B
            j_end = start

cnt = 1
while lst:
    order = h.heappop(lst)
    if order[1] == 'B':
        sangmin.append(cnt)
    else:
        jisu.append(cnt)
    cnt += 1

print(len(sangmin))
print(*sangmin)
print(len(jisu))
print(*jisu)
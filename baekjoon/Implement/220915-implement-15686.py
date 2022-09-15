import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
chics = []
peeps = []

for i in range(N):
    lines = list(map(int,input().split()))
    for j in range(N):
        if lines[j] == 2:
            chics.append((i,j))
        elif lines[j] == 1:
            peeps.append((i,j))

minv = float('inf')
for chic in combinations(chics,M):
    sumv = 0
    for peep in peeps:
        sumv += min([abs(peep[0]-i[0])+abs(peep[1]-i[1]) for i in chic])
        if minv <= sumv: break
    minv = min(minv,sumv)

print(minv)
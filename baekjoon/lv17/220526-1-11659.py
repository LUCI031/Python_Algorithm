import sys
input=sys.stdin.readline

N,M = map(int, input().split())
lst = list(map(int, input().split()))
c = [0, lst[0]]

for i in range(1,N):
    c.append(c[-1]+lst[i])
    
for _ in range(M):
    a,b = map(int, input().split())
    print(c[b]-c[a-1])
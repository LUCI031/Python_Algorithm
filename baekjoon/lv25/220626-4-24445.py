import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
V = [0 for _ in range(N + 1)]
E = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(1, N + 1):
    E[i].sort(reverse=True)

def bfs(graph,R,visited):
    que = deque([R])
    visited[R] = 1
    cnt = 2
    
    while que:
        R = que.popleft()
        
        for i in graph[R]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = cnt
                cnt += 1

bfs(E,R,V)

for i in range(1, N + 1):
    print(V[i])
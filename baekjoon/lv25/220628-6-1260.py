import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
d_ans = []
b_ans = []
def dfs(V, E, R, order):
    global d_ans
    V[R] = order
    edges = E[R]
    d_ans.append(R)

    for edge in edges:
        if V[edge] == 0:
            order = dfs(V, E, edge, order + 1)
    return order

def bfs(graph,R,visited):
    que = deque([R])
    visited[R] = 1
    cnt = 2
    
    while que:
        R = que.popleft()
        b_ans.append(R)
        
        for i in graph[R]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = cnt
                cnt += 1


N,M, R = map(int, input().split())

V1 = [0 for _ in range(N + 1)]
E1 = [[] for _ in range(N + 1)]
V2 = [0 for _ in range(N + 1)]
E2 = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E1[u].append(v)
    E2[u].append(v)
    E1[v].append(u)
    E2[v].append(u)

for i in range(len(E1)):
    E1[i].sort()
    E2[i].sort()
    
order = 1
dfs(V1, E1, R, order)
print(*d_ans)

bfs(E2, R, V2)
print(*b_ans)
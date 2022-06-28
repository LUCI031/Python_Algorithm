import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

cnt = 0
def dfs(V, E, R, order):
    global cnt
    V[R] = order
    edges = E[R]

    for edge in edges:
        if V[edge] == 0:
            cnt += 1
            order = dfs(V, E, edge, order + 1)
    return order


N = int(input())
M = int(input())

V = [0 for _ in range(N + 1)]
E = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(1, N + 1):
    E[i].sort()

order = 1
dfs(V, E, 1, order)

print(cnt)
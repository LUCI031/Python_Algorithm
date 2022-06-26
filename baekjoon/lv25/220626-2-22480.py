import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(V, E, R, order):
    V[R] = order
    edges = E[R]

    for edge in edges:
        if V[edge] == 0:
            order = dfs(V, E, edge, order + 1)
    return order


# 입력값 처리
N, M, R = map(int, input().split())
V = [0 for _ in range(N + 1)]
E = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(1, N + 1):
    E[i].sort(reverse=True)

# dfs 탐색 시작
order = 1
dfs(V, E, R, order)

for i in range(1, N + 1):
    print(V[i])
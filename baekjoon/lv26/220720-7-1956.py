import sys
input = sys.stdin.readline

inf = float('inf')
v,e = map(int,input().split())
graph = [[inf for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    if graph[a][b] > c:
        graph[a][b] = c


def floyd_warshall():
    for c in range(1,v+1):
        for a in range(1,v+1):
            for b in range(1,v+1):
                if graph[a][b] > graph[a][c]+ graph[c][b]:
                    graph[a][b] = graph[a][c] + graph[c][b]

answer = inf

floyd_warshall()

for i in range(1,v+1):
    answer = min(answer,graph[i][i])

if answer == inf:
    print(-1)
else:
    print(answer)
import sys
input = sys.stdin.readline

INF = int(1e9)

N,M = map(int,input().split())
edges = []
dist = [INF] * (N+1)

for _ in range(M):
    start,end,time = map(int,input().split())
    edges.append((start,end,time))
    

def bellman(start):
    dist[start] = 0

    for i in range(N):
        for j in range(M):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]

            if dist[cur_node] != INF and dist[next_node] > dist[cur_node]+edge_cost:
                dist[next_node] = dist[cur_node] + edge_cost

                if i == N-1:
                    return True
    return False

neg_cycle = bellman(1)

if neg_cycle:
    print('-1')
else:
    for i in range(2,N+1):
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])
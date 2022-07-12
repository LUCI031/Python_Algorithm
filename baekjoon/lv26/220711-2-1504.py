import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]

answer = [INF] * (V+1)
que = []

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

stop1, stop2 = map(int,input().split())

def dijkstra(start, end):
    answer = [INF] * (V+1)
    answer[start] = 0
    heapq.heappush(que, [0,start])

    while que:
        cur_w, cur_node = heapq.heappop(que)

        if answer[cur_node] < cur_w:
            continue

        for n_node, weight in graph[cur_node]:
            next_w = cur_w + weight

            if next_w < answer[n_node]:
                answer[n_node] = next_w
                heapq.heappush(que, [next_w,n_node])
    return answer[end]


path1 = dijkstra(1,stop1) + dijkstra(stop1,stop2) + dijkstra(stop2,V)
path2 = dijkstra(1,stop2) + dijkstra(stop2,stop1) + dijkstra(stop1,V)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1,path2))
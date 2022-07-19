import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, graph):
    answer = [INF] * (n+1)
    answer[start] = 0
    que = []
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
    return answer

INF = float('inf')
n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    edges[a].append((b,c))

for i in range(1,n+1):
    ans = dijkstra(i,edges)
    for k in ans[1:]:
        if k == INF:
            print(0,end=' ')
        else:
            print(k,end=' ')
    print()
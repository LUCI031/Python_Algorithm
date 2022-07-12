# https://my-coding-notes.tistory.com/200

import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

answer = [INF] * (V+1)
que = []

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

def dijkstra(start):
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

dijkstra(K)

for i in answer[1:]:
    print(i if i != INF else "INF")
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, end, graph):
    answer = [INF] * (n+1)
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
    return answer
    
INF = float('inf')
T = int(input())

for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    
    dest = []
    que = []
    ans = []

    for _ in range(m):
        a,b,d = map(int,input().split())
        if (a==g and b==h) or (a==h and b==g):
            d -= 0.1
        graph[a].append([b,d])
        graph[b].append([a,d])

    for _ in range(t):
        dest.append(int(input()))
    dest.sort()
    ans_d = dijkstra(s,n,graph)

    for target in dest:
        if ans_d[target] != INF and type(ans_d[target]) == float:
            print(target, end=' ')
    print()
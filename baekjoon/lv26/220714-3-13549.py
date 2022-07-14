import sys
from collections import deque
input = sys.stdin.readline

start,goal = map(int,input().split())
v = [-1 for _ in range(100001)]
v[start] = 0
que = deque()
que.append(start)

while que:
    cur = que.popleft()
    if cur == goal:
        print(v[goal])
        break
    dx = [cur,-1,1]
    for i in range(3):
        nx_node = cur+dx[i]
        if nx_node < 0 or nx_node > 100000 or v[nx_node] >= 0:
            continue
        if i == 0:
            v[nx_node] = v[cur]
            que.append(nx_node)
        else:
            v[nx_node] = v[cur]+1
            que.append(nx_node)






# 실패

# INF = float('inf')
# start,goal = map(int,input().split())

# loc = [0] * 100001
# v = [0] * 100001
# loc[start] = 0
# v[start] = 1
# que = deque()
# que.append([0,start])
# status = True

# while que and status:
#     cur_w, cur_node = que.popleft()
#     if cur_node == goal:
#         break
#     dx = [cur_node,-1,1]
#     for i in range(3):
#         nx_node = cur_node+dx[i]
#         if nx_node < 0 or nx_node > 100000 or v[nx_node] > 0:
#             continue
#         if i != 0:
#             loc[nx_node] += cur_w+1
#         else:
#             loc[nx_node] = cur_w
#         v[nx_node] += 1
#         if nx_node == goal:
#             staus = False
#             break
#         if nx_node < goal*2:
#             if i != 0:
#                 que.append([loc[nx_node],nx_node])
#             else:
#                 que.appendleft([loc[nx_node],nx_node])

# print(loc[goal])
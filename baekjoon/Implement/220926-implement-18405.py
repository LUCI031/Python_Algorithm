import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
que = []
lst = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(N):
    nums = list(map(int,input().split()))
    lst.append(nums)
    for j in range(N):
        if nums[j] > 0:
            que.append((nums[j],i,j))
    
S,X,Y = map(int,input().split())
que = deque(sorted(que))
for _ in range(S):
    n_que = []
    while que:
        num = que.popleft()
        for i in range(4):
            nx = num[1]+dx[i]
            ny = num[2]+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if lst[nx][ny] == 0:
                    lst[nx][ny] = num[0]
                    n_que.append((num[0],nx,ny))
    que = deque(sorted(n_que))
X -= 1
Y -= 1
if lst[X][Y] > 0:
    print(lst[X][Y])
else:
    print(0)
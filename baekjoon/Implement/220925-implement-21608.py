import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
P = N*N
classrm = [[0]*N for _ in range(N)]
likerm = [[] for _ in range((N**2)+1)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(P):
    arr = list(map(int,input().split()))
    like = arr[1:]
    likerm[arr[0]] = like
    if P == 0:
        classrm[1][1] = arr[0]
        continue
    tmp = []
    for i in range(N):
        for j in range(N):
            sum_like, sum_empty = 0, 0
            if classrm[i][j] != 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if classrm[nx][ny] in like:
                        sum_like += 1
                    if classrm[nx][ny] == 0:
                        sum_empty += 1
            tmp.append((sum_like,sum_empty,(i,j)))
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2]))
    classrm[tmp[0][2][0]][tmp[0][2][1]] = arr[0]

    sum_answer = 0

    for i in range(N):
        for j in range(N):
            answer = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k] 
                if 0 <= nx < N and 0 <= ny < N:
                    if classrm[nx][ny] in likerm[classrm[i][j]]:
                        answer += 1
                        continue
            if answer != 0:
                sum_answer += (10 ** (answer-1))
print(sum_answer)
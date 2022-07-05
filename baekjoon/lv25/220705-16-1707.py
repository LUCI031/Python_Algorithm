import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, group):
    que = deque([start]) # 시작 정점 값 큐에 담음
    v[start] = group # 시작 정점 그룹 설정
    while que: # bfs 실행
        
        R = que.popleft()
        
        for i in lst[R]:
            if not v[i]: # 정점 방문 확인
                que.append(i)
                v[i] = -1 * v[R] # 상위 정점과 다른 그룹으로 편성
            elif v[i] == v[R]: # 방문 했는데 같은 그룹이면
                return False
    return True

for _ in range(int(input())):
    V,E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    v = [False for _ in range(V+1)]
    
    for _ in range(E):
        a,b, = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
        
    for i in range(1,V+1):
        if not v[i]:
            result = bfs(i,1) # 방문한 정점 아니면 bfs 수행
            if not result:
                break
    
    print('YES' if result else 'NO')
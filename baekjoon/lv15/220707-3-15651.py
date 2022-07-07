import sys
input=sys.stdin.readline

N,M = map(int,input().split())
lst = []

def dfs(cnt):
    if cnt -1 == M:
        print(' '.join(map(str,lst)))
        return
    for i in range(1,N+1):
        lst.append(i)
        dfs(cnt+1)
        lst.pop()

dfs(1)
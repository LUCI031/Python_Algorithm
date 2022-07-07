import sys
input=sys.stdin.readline

N,M = map(int,input().split())
lst = []

def dfs(cnt):
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    for i in range(1,N+1):
        if len(lst) > 0:
            if lst[-1] <= i:
                lst.append(i)
                dfs(cnt+1)
                lst.pop()    
        else:        
            lst.append(i)
            dfs(cnt+1)
            lst.pop()

dfs(1)
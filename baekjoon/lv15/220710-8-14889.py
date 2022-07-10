import sys
input=sys.stdin.readline

N = int(input())
lst = []
select = [0 for _ in range(N)]
ans = sys.maxsize

for i in range(N):
    lst.append(list(map(int,input().split())))


def dfs(idx, cnt):
    global ans
    if cnt == N//2:
        start, link = 0,0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    start += lst[i][j]
                elif not select[i] and not select[j]:
                    link += lst[i][j]
        ans = min(ans,abs(start-link))

    for i in range(idx,N):
        if select[i]:
            continue
        select[i] = 1
        dfs(i+1, cnt+1)
        select[i] = 0


dfs(0,0)
print(ans)
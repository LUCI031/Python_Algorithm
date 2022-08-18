import sys, math
import heapq as h
input = sys.stdin.readline

lst = []

N, H, T = map(int,input().split())
cnt = 0
for i in range(N):
    Hs = int(input())
    h.heappush(lst,-Hs)

for i in range(T):
    num = -(h.heappop(lst))
    if num < H:
        h.heappush(lst,-num)
        break
    elif num <= 1:
        h.heappush(lst,-num)
    else:
        num//= 2
        h.heappush(lst,-num)
        cnt += 1


num = -h.heappop(lst)
if num < H:
    print('YES')
    print(cnt)
else:
    print('NO')
    print(num)
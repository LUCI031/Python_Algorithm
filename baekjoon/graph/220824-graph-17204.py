import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int,input().split())

order = [0]
to = defaultdict(int)
cnt = 1

for i in range(N):
    to[i] = int(input())
frm = 0

while True:
    if to[frm] == M:
        print(cnt)
        exit()
    if to[frm] in order:
        print(-1)
        exit()
    else:
        order.append(to[frm])
        frm = to[frm]
        cnt += 1
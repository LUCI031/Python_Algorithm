import sys
from collections import deque
input = sys.stdin.readline

N,W,L = map(int,input().split())
bridge = [0 for _ in range(W)]
start = list(map(int,input().split()))
start = deque(start)
cnt = 0

while True:
    if sum(bridge) == 0 and not start:
        print(cnt)
        exit()

    cnt += 1
    if bridge[0] != 0:
        bridge[0] = 0
    for i in range(W-1):
        if bridge[i+1] != 0:
            bridge[i] = bridge[i+1]
            bridge[i+1] = 0

    if start and sum(bridge)+start[0] <= L and bridge[-1] == 0:
        bridge[-1] = start.popleft()
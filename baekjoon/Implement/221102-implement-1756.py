import sys
from collections import deque, defaultdict
input = sys.stdin.readline

D, N = map(int,input().split())
oven = list(map(int,input().split()))
for i in range(D-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]
pizza = list(map(int,input().split()))
pos = D
cur = 0

for i in range(D-1,-1,-1):
    if pizza[cur] > oven[i]:
        continue
    cur += 1
    if cur >= N:
        print(i+1)
        exit()

print(0)
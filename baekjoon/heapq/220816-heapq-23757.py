import sys
import heapq as h
input = sys.stdin.readline

N, M = map(int,input().split())

gifts_org = list(map(int,input().split()))
gifts_h = []
ispre = False
kids = list(map(int,input().split()))

for gift in gifts_org:
    h.heappush(gifts_h,-gift)

for kid in kids:
    gift = -(h.heappop(gifts_h))
    if gift - kid < 0:
        ispre = True
        break
    h.heappush(gifts_h, -(gift-kid))

if ispre:
    print(0)
else:
    print(1)
import sys
input=sys.stdin.readline

N, M = map(int,input().split())

cards = list(map(int, input().split()))
cards.sort()
picked = sum(cards[0:3])
for i in cards[::-1]:
    for j in cards[-2::-1]:
        for k in cards[-3::-1]:
            if i==j or i==k or j==k:
                pass
            elif picked < i+j+k <= M:
                picked = i+j+k

print(picked)
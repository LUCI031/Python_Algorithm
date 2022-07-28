import sys
input = sys.stdin.readline

a,b = map(int,input().split())

fav = []
N = int(input())
for _ in range(N):
    fav.append(int(input()))

dis = abs(b-a)

for i in fav:
    if abs(b-i)+1 < dis:
        dis = abs(b-i)+1

print(dis)
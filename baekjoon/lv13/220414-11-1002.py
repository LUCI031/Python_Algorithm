# 문제가 잘 이해가 안되서 거의 보면서 품
# 내접 외접 등등
import sys, math
input=sys.stdin.readline

T = int(input())

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 == distance:
        print(1)
    elif abs(r1-r2) < distance < abs(r1+r2):
        print(2)
    else:
        print(0)
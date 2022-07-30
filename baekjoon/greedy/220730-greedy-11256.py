import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cnt = 0
    boxes = []
    J,N = map(int,input().split())
    for _ in range(N):
        a,b = map(int,input().split())
        boxes.append((a*b))
    boxes.sort()
    while J > 0 and len(boxes)>0:
        box = boxes.pop()
        if J > box:
            J -= box
            cnt += 1
        else:
            cnt += 1
            print(cnt)
            break
import sys
from collections import deque
input=sys.stdin.readline

N = int(input())

for _ in range(N):
    cnt = 0
    order = list(map(int, input().split()))
    lst = deque([(x,i) for i, x in enumerate(list(map(int, input().split())))])
    while True:
        if lst[0][0] == max(lst)[0]:
            cnt += 1
            if lst[0][1] == order[1]:
                print(cnt)
                break
            else:
                lst.popleft()
        else:
            lst.append(lst.popleft())
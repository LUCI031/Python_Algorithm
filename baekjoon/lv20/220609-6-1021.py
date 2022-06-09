import sys
from collections import deque
input=sys.stdin.readline

N,M = map(int, input().split())
targets = deque(list(map(int, input().split())))
lst = deque([i for i in range(1,N+1)])
cnt = 0

while targets:
    target = targets[0]
    if target == lst[0]:
        lst.popleft()
        targets.popleft()
    else:
        if lst.index(target) > len(lst)/2:
            while target != lst[0]:
                lst.appendleft(lst.pop())
                cnt += 1
        else:
            while target != lst[0]:
                lst.append(lst.popleft())
                cnt += 1
print(cnt)

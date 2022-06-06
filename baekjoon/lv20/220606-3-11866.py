import sys
from collections import deque
input=sys.stdin.readline

N = list(map(int,input().split()))
lst = deque([i for i in range(1,N[0]+1)])
cnt = 1
result = []
while lst:
    if cnt != N[1]:
        lst.append(lst.popleft())
        cnt += 1
    else:
        result.append(lst.popleft())
        cnt = 1

print('<', end='')
print(*result,sep=', ',end='')
print('>')
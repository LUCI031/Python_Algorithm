import sys
from collections import deque
input=sys.stdin.readline

N = int(input())
stack = deque()

for i in range(N):
    lst = list(map(str,input().split()))
    if len(lst) == 1:
        if lst[0] == 'pop':
            if stack:
                print(stack.popleft())
            else:
                print(-1)
        elif lst[0] == 'size':
            print(len(stack))
        elif lst[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif lst[0] == 'front':
            if stack:
                print(stack[0])
            else:
                print(-1)
        elif lst[0] == 'back':
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        stack.append(lst[1])
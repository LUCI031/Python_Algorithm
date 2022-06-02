import sys
input=sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    lst = list(map(str,input().split()))
    if len(lst) == 1:
        if lst[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif lst[0] == 'size':
            print(len(stack))
        elif lst[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif lst[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        stack.append(lst[1])
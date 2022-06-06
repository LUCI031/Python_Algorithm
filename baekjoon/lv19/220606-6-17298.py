import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
stack=deque()
result=[-1]*n
for i in range(n):
    while stack:
        if lst[i]>lst[stack[-1]]:
            result[stack.pop()]=lst[i]            
        else:
            break
    stack.append(i)

print(*result)
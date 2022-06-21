import sys
from bisect import bisect_left

l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]

for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[bisect_left(stack, a)] = a

print(len(stack)-1)
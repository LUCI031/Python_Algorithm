import sys
input = sys.stdin.readline

lst = list(input().strip())
stack = []
temp = 1
res = 0

for i in range(len(lst)):
    if lst[i] == '(':
        temp *= 2
        stack.append(lst[i])
    elif lst[i] == '[':
        temp *= 3
        stack.append(lst[i])

    elif lst[i] == ')':
        if not stack or stack[-1] == '[':
            print(0)
            exit()
        if lst[i-1] == '(':
            res += temp
        temp //= 2
        stack.pop()
    
    else:
        if not stack or stack[-1] == '(':
            print(0)
            exit()
        if lst[i-1] == '[':
            res += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
    exit()
print(res)
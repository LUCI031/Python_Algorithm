import sys
input = sys.stdin.readline

cnts = []
def checker(lst):
    cnt1 = 0
    new_stack = []
    for i in range(len(lst)):
        if lst[i] == '{':
            if i+1 < len(lst) and lst[i+1] == '}':
                cnt1 += 1
            else:
                new_stack.append(lst[i])
        else:
            if i-1 >= 0 and lst[i-1] == '{':
                cnt1 += 1
            else:
                new_stack.append(lst[i])
    if cnt1 != 0:
        return checker(new_stack)
    else:
        return new_stack

while True:
    cnt = 0
    lst = list(input().strip())
    if '-' in lst:
        for i in range(len(cnts)):
            print(f'{i+1}. {cnts[i]}')
        exit()
    else:
        stack = checker(lst)
        stack2 = []
        for sign in stack:
            if not stack2:
                if sign == '{':
                    stack2.append(sign)
                else:
                    cnt += 1
                    stack2.append('{')
            else:
                if sign == '}':
                    stack2.pop()
                else:
                    cnt += 1
                    stack2.pop()
    cnts.append(cnt)
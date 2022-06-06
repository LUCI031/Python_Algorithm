import sys
input=sys.stdin.readline


while True:
    lst = []
    state = True
    a = input()
    if a == '.':
        break
    for i in a:
        if i == '(' or i == '[':
            lst.append(i)
        elif i == ')':
            if not lst or lst[-1] == '[':
                state = False
                break
            else:
                lst.pop()
        elif i == ']':
            if not lst or lst[-1] == '(':
                state = False
                break
            else:
                lst.pop()
    if state==True and not lst:
        print('yes')
    else:
        print('no')
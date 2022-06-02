import sys
input=sys.stdin.readline

T = int(input())

for i in range(T):
    lst1 = []
    lst2 = []
    case = input().strip()
    for j in range(len(case)):
        if case[j] == '(':
            lst1.append(1)
        else:
            if lst1:
                lst1.pop()
            else:
                lst2.append(1)
    if lst1 or lst2:
        print('NO')
    else:
        print('YES')        
    
import sys
from collections import deque
input=sys.stdin.readline

N = int(input())

for _ in range(N):
    cnt = 1
    cmd = input().strip()
    num = int(input())
    ques = list(input().rstrip()[1:-1].split(','))
    que2 = deque()

    if num == 0:
        que1 = deque()
    else:
        que1 = deque(ques)
        for k in range(len(que1)-1,-1,-1):
            que2.append(que1[k])

    for i in cmd:
        if i == 'R':
            if cnt == 1:
                cnt = 2
            elif cnt == 2:
                cnt = 1
        else:
            if cnt == 1 and que1:
                que1.popleft()
                que2.pop()
            elif cnt == 2 and que1:
                que2.popleft()
                que1.pop()
            else:
                cnt = 3
                break
    
    if cnt == 1:
        print('[',end='')
        print(*que1,sep=',',end='')
        print(']')
    elif cnt == 2:
        print('[',end='')
        print(*que2,sep=',',end='')
        print(']')
    elif cnt == 3:
        print('error')

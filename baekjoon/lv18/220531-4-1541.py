import sys
from collections import deque
input=sys.stdin.readline

ques = input().strip()
num = []
num_lst = []
pm = []
stack = 0
state = 1

for i in ques:
    if str.isdigit(i):
        num.append(i)
    else:
        num_lst.append(int(''.join(num)))
        num = []
        pm.append(i)
num_lst.append(int(''.join(num)))

num_lst = deque(num_lst)
ans = num_lst.popleft()

for i in range(len(num_lst)):
    if state == 1 and pm[i] == '+':
        ans += num_lst[i]
    elif state == 0 and pm[i] == '+':
        ans -= num_lst[i]
    elif state == 1 and pm[i] == '-':
        state = 0
        ans -= num_lst[i]
    elif state == 0 and pm[i] == '-':
        ans -= num_lst[i]
        
print(ans)
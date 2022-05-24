import sys
from collections import Counter as ct
input=sys.stdin.readline

N,M = map(int, input().split())
lst = []
cnt = 0
answer = []
for _ in range(N+M):
    lst.append(input().strip())

lst_cnt = ct(lst)

for i,j in lst_cnt.items():
    if j > 1:
        cnt += 1
        answer.append(i)

print(cnt)
answer.sort()
for i in answer:
    print(i)
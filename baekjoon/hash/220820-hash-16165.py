import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int,input().split())
g_lst = defaultdict(str)
m_lst = defaultdict(list)
for i in range(N):
    group = str(input().strip())
    num = int(input())
    for i in range(num):
        member = str(input().strip())
        m_lst[group].append(member)
        g_lst[member] = group
    m_lst[group].sort()
for i in range(M):
    ques = str(input().strip())
    num = int(input())
    if num == 1:
        print(g_lst[ques])
    else:
        for member in m_lst[ques]:
            print(member)
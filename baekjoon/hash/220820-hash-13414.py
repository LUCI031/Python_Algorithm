import sys
from collections import defaultdict
input = sys.stdin.readline

K, L = map(int,input().split())
lst = defaultdict(int)
for i in range(L):
    s_id = str(input().strip())
    if len(s_id) == 8:
        lst[s_id] = i

lst = sorted(lst.items(), key= lambda item: item[1])
for i in range(K):
    if len(lst) > i:
        print(lst[i][0])
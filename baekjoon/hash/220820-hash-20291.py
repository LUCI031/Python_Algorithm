import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
lst = defaultdict(int)
for _ in range(N):
    _,ext = map(str,input().strip().split('.'))
    lst[ext] += 1

lst = sorted(lst.items(),key = lambda x: x[0])

for res in lst:
    print(res[0],res[1])
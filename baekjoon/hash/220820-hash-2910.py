import sys
from collections import defaultdict
input = sys.stdin.readline

N,C = map(int,input().split())
lst = list(map(int,input().split()))
dics = defaultdict(list)
sets = set(lst)
nums = []

for i in range(N):
    if lst[i] not in nums:
        nums.append(lst[i])
        dics[lst[i]] = [-1,i]
    else:
        dics[lst[i]][0] -= 1

dics = sorted(dics.items(), key = lambda item: item[1][0])

for res in dics:
    for _ in range(-res[1][0]):
        print(res[0],sep = ' ',end = ' ')
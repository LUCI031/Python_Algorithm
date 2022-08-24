import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
res = []
dics = defaultdict(int)
for i in range(1,N+1):
    dics[i] = int(input())

def dfs(num, lst):
    if dics[num] not in lst:
        lst.append(dics[num])
        return dfs(dics[num],lst)
    else:
        return len(lst)

for i in range(1,N+1):
    lst = [i]
    ans = dfs(i,lst)
    res.append((-ans,i))

res.sort()
print(res[0][1])
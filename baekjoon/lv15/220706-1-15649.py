import sys
input=sys.stdin.readline
from itertools import permutations as perm


N,M = map(int,input().split())

lst = [i for i in range(1,N+1)]

result = list(perm(lst,M))
result.sort()

for i in range(len(result)):
    print(*result[i])
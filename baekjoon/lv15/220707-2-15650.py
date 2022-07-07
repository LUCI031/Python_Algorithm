import sys
input=sys.stdin.readline
from itertools import combinations as comb


N,M = map(int,input().split())

lst = [i for i in range(1,N+1)]

result = list(comb(lst,M))
result.sort()

for i in range(len(result)):
    print(*result[i])
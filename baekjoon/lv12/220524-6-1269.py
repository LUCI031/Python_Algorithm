import sys
from collections import Counter as ct
input=sys.stdin.readline

N,M = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
cnt = 0
dict = ct(lst1+lst2)

for i,j in dict.items():
    if j == 1:
        cnt += 1
        
print(cnt)
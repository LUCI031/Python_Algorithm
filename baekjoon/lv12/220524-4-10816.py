import sys
from collections import Counter as ct
input=sys.stdin.readline

dict = {}

N = int(input())
dict = ct(map(int,input().split()))

M = int(input())
lst = list(map(int,input().split()))


for i in range(M):
    if lst[i] in dict:
        print(dict[lst[i]],end=' ')
    else:
        print(0,end=' ')

import sys
input=sys.stdin.readline

N = int(input())
lst = ['*']*N

for i in range(N):
    lst[i] = (str(input()).rstrip())
    
lst = sorted(list(set(lst)))
lst.sort(key = len)

for j in lst:
    print(j)
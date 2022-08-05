import sys
input = sys.stdin.readline

N,L = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()

start = lst[0] 
cnt = 1

for i in lst[1:]:
    if i-start >= L:
        cnt += 1
        start = i

print(cnt)
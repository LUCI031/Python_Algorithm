import sys
input = sys.stdin.readline

N,M = map(int,input().split())
if N == 0:
    print(0)
    exit()
lst = list(map(int,input().split()))
cnt = 0
nums = 0

for i in lst:
    if nums + i <= M:
        nums = nums + i
    else:
        cnt += 1
        nums = i

print(cnt+1)
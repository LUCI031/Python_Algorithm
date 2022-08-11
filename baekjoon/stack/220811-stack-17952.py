import sys
input = sys.stdin.readline

N = int(input())
scores = []
res = 0
for i in range(N):
    lst = list(map(int,input().split()))
    if len(lst) == 3:
        scores.append([lst[1],lst[2]])
    if scores:
        scores[-1][1] -= 1
        if scores[-1][1] == 0:
            aa = scores.pop()
            res += aa[0]

print(res)
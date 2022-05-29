import sys
n, m = map(int, input().split())
arr_n = list(map(int, sys.stdin.readline().split()))
arr_m = [0 for _ in range(m)]

s = 0
num = 0
for i in range(n):
    s += arr_n[i]
    res = s % m

    if res == 0:
        num += 1
    
    arr_m[res] += 1


for i in range(m):
    if arr_m == 0:
        continue

    num += arr_m[i] * (arr_m[i] - 1) / 2

print(int(num))
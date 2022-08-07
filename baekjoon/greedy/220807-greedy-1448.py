import sys
input = sys.stdin.readline

lst = []

N = int(input())
for _ in range(N):
    lst.append(int(input()))
lst.sort()

for i in range(N-1,1,-1):
    if lst[i] < lst[i-1] + lst[i-2]:
        print(lst[i] + lst[i-1] + lst[i-2])
        exit()
print(-1)
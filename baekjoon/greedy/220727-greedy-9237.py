import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int,input().split()))

lst.sort(reverse=True)

for i in range(N):
    lst[i] = 1 + lst[i] + (i+1)

print(max(lst))
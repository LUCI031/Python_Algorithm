import sys
input=sys.stdin.readline

N = int(input())
a = set(list(map(int,input().split())))
M = int(input())
b = list(map(int,input().split()))

for i in range(M):
    if b[i] in a:
        print(1)
    else:
        print(0)
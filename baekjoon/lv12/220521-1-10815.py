import sys
input=sys.stdin.readline

dict = {}

N = int(input())
lst1 = list(map(int,input().split()))
for i in range(N):
    dict[lst1[i]] = 0

M = int(input())
lst2 = list(map(int,input().split()))

for i in range(M):
    if lst2[i] in dict:
        print(1,end=' ')
    else:
        print(0,end=' ')

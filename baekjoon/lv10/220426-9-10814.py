import sys
input=sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    x,y = map(str, input().split())
    lst.append([int(x),i,y])
lst = sorted(lst, key=lambda x: (x[0],x[1]))
for j in range(len(lst)):   
    print(lst[j][0], lst[j][2])
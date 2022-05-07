import sys
input=sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    x,y = map(int,input().split())
    arr.append((y,x))

arr.sort()

for j in range(N):
    print(arr[j][1],arr[j][0])
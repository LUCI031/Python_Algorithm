import sys
input=sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(int,input().split())))
    
for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            lst[i][j] = lst[i][j] + lst[i-1][j]
        elif j == i:
            lst[i][j] = lst[i][j] + lst[i-1][j-1]
        else:
            lst[i][j] = max(lst[i][j] + lst[i-1][j],lst[i][j] + lst[i-1][j-1])

print(max(lst[-1]))
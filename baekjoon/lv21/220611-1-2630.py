import sys
input=sys.stdin.readline

N = int(input())

def recur(x,y,N):
    flag = False
    
    for i in range(x,x+N):
        if flag:
            break
    
        for j in range(y,y+N):
            if lst[x][y] != lst[i][j]:
                recur(x, y, N // 2)
                recur(x, y + N // 2, N // 2)
                recur(x + N // 2, y, N // 2)
                recur(x + N // 2, y + N // 2, N // 2)
                flag = True
                break
        
    if not flag:
        if lst[x][y] == 0:
            count[0] += 1
        else:
            count[1] += 1

lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
    
count= [0,0]

recur(0,0,N)
for i in count:
    print(i)

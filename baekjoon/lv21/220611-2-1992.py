import sys
input=sys.stdin.readline

def recur(x,y,N):
    flag = False

    for i in range(x,x+N):
        if flag:
            break

        for j in range(y,y+N):
            if lst[x][y] != lst[i][j]:
                print('(',end='')
                recur(x, y, N // 2)
                recur(x, y + N // 2, N // 2)
                recur(x + N // 2, y, N // 2)
                recur(x + N // 2, y + N // 2, N // 2)
                print(')',end='')
                flag = True
                break
        
    if not flag:
        if lst[x][y] == 0:
            print(0,end='')
        else:
            print(1,end='')
            

N = int(input())
lst = []
for _ in range(N):
    a = input().strip()
    temp = []
    for k in a:
        temp.append(int(k))
    lst.append(temp)
    
recur(0,0,N)
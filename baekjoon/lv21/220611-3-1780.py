import sys
input=sys.stdin.readline

def recur(x,y,N):
    flag = False

    for i in range(x,x+N):
        if flag:
            break

        for j in range(y,y+N):
            if lst[x][y] != lst[i][j]:
                recur(x,y,N//3)
                recur(x+N//3,y,N//3)
                recur(x,y+N//3,N//3)
                recur(x+N//3,y+N//3,N//3)
                recur(x,y+(N//3*2),N//3)
                recur(x+(N//3*2),y,N//3)
                recur(x+N//3,y+(N//3*2),N//3)
                recur(x+(N//3*2),y+N//3,N//3)
                recur(x+(N//3*2),y+(N//3*2),N//3)
                flag = True
                break
        
    if not flag:
        if lst[x][y] == -1:
           cnt[0] += 1
        elif lst[x][y] == 0:
            cnt[1] += 1
        else:
            cnt[2] += 1
        
            

N = int(input())
lst = []
cnt = [0,0,0]
for _ in range(N):
    lst.append(list(map(int,input().split())))
    
recur(0,0,N)
for i in cnt:
    print(i)
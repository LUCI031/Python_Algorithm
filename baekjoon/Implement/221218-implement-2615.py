import sys
input = sys.stdin.readline
six = [(-1,0),(-1,-1),(0,-1),(1,-1)]
dir = [(1,0),(1,1),(0,1),(-1,1)]
def checker(num,cnt,x,y,curr):
    global flag
    nx = x+curr[0]
    ny = y+curr[1]
    if 0 <= nx < 19 and 0 <= ny < 19:
        if num == board[nx][ny]:
            if cnt < 5:
                checker(num,cnt+1,nx,ny,curr)
            else:
                flag = False
                return
    if cnt == 5:
        flag = True
        return


board = []
for _ in range(19):
    board.append(list(input().split()))
flag = False
flag2 = 'A'
for i in range(19):
    for j in range(19):
        if board[i][j] == '1' or board[i][j] == '2':
            for k in range(4):
                checker(board[i][j],1,i,j,dir[k])
                if flag:
                    kx = i+six[k][0]
                    ky = j+six[k][1]
                    if 0 <= kx < 19 and 0 <= ky < 19:
                        if board[kx][ky] == board[i][j]:
                            flag2 = 'B'
                    if flag2 == 'A':
                        if board[i][j] == '1':
                            print(1)
                        else:
                            print(2)
                        print(i+1,j+1)
                        exit()
                    else:
                        flag = False
                        flag2 = 'A'

print(0)
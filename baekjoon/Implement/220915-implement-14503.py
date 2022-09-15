import sys
input = sys.stdin.readline

N,M = map(int,input().split())
x,y,d = map(int,input().split())
v_map = [list(map(int,input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
v[x][y] = 1
cnt = 1
turn_time = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global d
    d = (d-1)%4

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if v[nx][ny] == 0 and v_map[nx][ny] == 0:
        v[nx][ny] = 1
        cnt += 1
        x,y = nx,ny
        turn_time = 0
        continue

    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if v_map[nx][ny] == 0:
            x,y = nx,ny
        else: break
        turn_time = 0

print(cnt)
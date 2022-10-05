import sys
input = sys.stdin.readline

N,M = map(int,input().split())
bucket = []
coord = []

def checker(check,v):
    n_cloud = []
    for i in range(N):
        for j in range(N):
            if bucket[i][j] >= 2 and v[i][j] == 0:
                n_cloud.append((i,j))
                bucket[i][j] -= 2
    return n_cloud

for _ in range(N):
    bucket.append(list(map(int,input().split())))

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

c_dx = [1,1,-1,-1]
c_dy = [-1,1,1,-1]

clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for _ in range(M):
    v = [[0]*N for _ in range(N)]
    check2 = []
    d,s = map(int,input().split())
    d -= 1
    for cloud in clouds:
        c_x = (cloud[0]+(dx[d]*s))%N
        c_y = (cloud[1]+(dy[d]*s))%N
        bucket[c_x][c_y] += 1
        v[c_x][c_y] = 1
        check2.append((c_x,c_y))
    for chk in check2:
        cnt = 0
        for i in range(4):
            nx,ny = chk[0]+c_dx[i],chk[1]+c_dy[i]
            if 0 <= nx < N and 0 <= ny < N and bucket[nx][ny] > 0:
                cnt += 1
        bucket[chk[0]][chk[1]] += cnt
    clouds = checker(check2,v)

sums = 0
for i in range(N):
    sums += sum(bucket[i])

print(sums)
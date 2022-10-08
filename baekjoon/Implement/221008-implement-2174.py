import sys
from collections import deque
input = sys.stdin.readline

A,B = map(int,input().split())
N,M = map(int,input().split())

field = [[0 for _ in range(A)] for _ in range(B)]
robots = [0]
orders = []
direc = [(1,0),(0,1),(-1,0),(0,-1)]

def direcs(d,repeat):
    if d == 'N':
        return direc[(0+repeat)%4]
    elif d == 'E':
        return direc[(1+repeat)%4]
    elif d == 'S':
        return direc[(2+repeat)%4]
    else:
        return direc[(3+repeat)%4]

def direcs_change(d):
    if d == direc[0]:
        return 'N'
    elif d == direc[1]:
        return 'E'
    elif d == direc[2]:
        return 'S'
    else:
        return 'W'

for i in range(1,N+1):
    robot = list(map(str,input().split()))
    robots.append([int(robot[1])-1,int(robot[0])-1,robot[2]])
    field[int(robot[1])-1][int(robot[0])-1] = i

for _ in range(M):
    order = list(map(str,input().split()))
    orders.append([int(order[0]),order[1],int(order[2])])

orders = deque(orders)

while orders:
    order = orders.popleft()
    robot = robots[order[0]]
    robot_num = field[robot[0]][robot[1]]
    if order[1] == 'L':
        robot[2] = direcs_change(direcs(robot[2],-order[2]))
    elif order[1] == 'R':
        robot[2] = direcs_change(direcs(robot[2],order[2]))
    else:
        field[robot[0]][robot[1]] = 0
        for i in range(1,order[2]+1):
            new_x = robot[0]+(direcs(robot[2],0)[0]*i)
            new_y = robot[1]+(direcs(robot[2],0)[1]*i)
            if 0 <= new_x < B and 0 <= new_y < A:
                if field[new_x][new_y] != 0:
                    print(f"Robot {robot_num} crashes into robot {field[new_x][new_y]}")
                    exit()
            else:
                print(f"Robot {robot_num} crashes into the wall")
                exit()
        robot[0] = new_x
        robot[1] = new_y
        field[new_x][new_y] = robot_num

print("OK")
import sys
import copy
input = sys.stdin.readline

r,c,n = map(int,input().split())

def install_bomb():
    for i in range(r):
        tmp = input().strip()
        for j in range(c):
            bomb[i][j] = 0 if tmp[j] == '.' else 2

def result():
    for i in range(r):
        for j in range(c):
            tmp = '.' if bomb[i][j] == 0 else 'O'
            print(tmp,end='')
        print()

def fill_bomb():
    for i in range(r):
        for j in range(c):
            bomb[i][j] = 3 if bomb[i][j] == 0 else bomb[i][j] - 1

def bomb_explode(bomb):
    nx = [1,-1,0,0]
    ny = [0,0,1,-1]
    bomb2 = copy.deepcopy(bomb)
    for i in range(r):
        for j in range(c):
            if bomb[i][j] == 0:
                for k in range(4):
                    if 0 <= i+nx[k] < r and 0 <= j+ny[k] < c:
                        bomb2[i+nx[k]][j+ny[k]] = 0
    return bomb2

bomb = [[0 for _ in range(c)] for _ in range(r)]

install_bomb()
for _ in range(n-1):
    fill_bomb()
    bomb = bomb_explode(bomb)
result()
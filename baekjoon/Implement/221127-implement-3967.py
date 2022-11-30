import sys
input = sys.stdin.readline

# checks = [[0,2,5,7],[1,2,3,4],
#         [7,8,9,10],[1,5,8,11],
#         [4,6,9,11],[0,3,6,10]]

# lines = [input().strip() for _ in range(5)]

# cnt = 0
# lst = [[] for _ in range(12)]
# alpha = [False for _ in range(12)]
# words = 'ABCDEFGHIJKL'
# flag = False

# for i in range(5):
#     for j in range(9):
#         pos = lines[i][j]
#         if pos != '.':
#             if pos != 'x':
#                 lst[cnt].append(ord(pos)-64)
#                 alpha[ord(pos)-65] = True
#             cnt += 1

# def dfs(idx):
#     if idx < 12 and lst[idx]:
#         dfs(idx+1)
#     elif idx == 12:
#         confirm(lst)
#         if flag:
#             ending()
#         else:
#             return
#     for i in range(12):
#         if alpha[i]: continue
#         alpha[i] = True
#         lst[idx].append(i+1)
#         dfs(idx+1)
#         lst[idx] = []
#         alpha[i] = False

# def confirm(lst):
#     for check in checks:
#         sums = 0
#         for i in range(4):
#             sums += lst[check[i]][0]
#         if sums != 26:
#             return
#     flag = True

# def ending():
#     cnt = 0
#     for i in range(5):
#         res = []
#         for j in range(9):
#             pos = lines[i][j]
#             if pos == '.':
#                 res.append('.')
#             elif pos == 'x':
#                 res.append('1') #(chr(lst[cnt]+64))
#                 cnt += 1
#             else:
#                 res.append(pos)
#                 cnt += 1
#         print(*res,sep='')
#     exit()

# dfs(0)

# def convertAlpha(num):
#     return chr(num + 65)


# def convertNum(alpha):
#     return ord(alpha) - 65

# checks = [[0,2,5,7],[1,2,3,4],
#         [7,8,9,10],[1,5,8,11],
#         [4,6,9,11],[0,3,6,10]]
# dics = {0:[0,4],
#         1:[1,1],
#         2:[1,3],
#         3:[1,5],
#         4:[1,7],
#         5:[2,2],
#         6:[2,6],
#         7:[3,1],
#         8:[3,3],
#         9:[3,5],
#         10:[3,7],
#         11:[4,4]}

# def solution(tmp):
#     for check in checks:
#         val = 0
#         for k in range(4):
#             val += ord(grid[dics[check[k]][0]][dics[check[k]][1]])-64
#     if val == 26:
#         ret = ""
#         for i in tmp:
#             ret += "".join(i)
#         answer.append(ret)

#     return True


# def apply_perm(combi):
#     tmp = grid
#     for idx, pos in enumerate(x_pos):
#         tmp[pos[0]][pos[1]] = str(convertAlpha(combi[idx]))
#     return tmp


# def dfs(pick):
#     if pick == x_cnt:
#         if solution(apply_perm(combi)):
#             for i in range(0, 45, 9):
#                 print(answer[0][i : i + 9])
#             exit(0)
#         return
#     for i in range(12):
#         if not visited[i]:
#             visited[i] = True
#             combi.append(i)
#             dfs(pick + 1)
#             visited[i] = False
#             combi.pop()


# N = 5
# grid = []

# for i in range(5):
#     data = input()
#     grid.append(list(data))
# x_cnt = 0
# x_pos = []
# visited = [False] * 12
# answer = []


# for i in range(5):
#     for j in range(9):
#         if grid[i][j] == "x":
#             x_cnt += 1
#             x_pos.append((i, j))
#         if grid[i][j] != "x" and grid[i][j] != ".":
#             visited[convertNum(grid[i][j])] = True

# combi = []
# dfs(0)

##

def convertAlpha(num):
    return chr(num + 65)


def convertNum(alpha):
    return ord(alpha) - 65


def solution(tmp):
    now_c = 4
    val = 0
    for i in range(4):
        val += convertNum(tmp[i][now_c])
        now_c -= 1
    if val + 4 != 26:
        return False

    val = 0
    for i in range(1, 9, 2):
        val += convertNum(tmp[3][i])
    if val + 4 != 26:
        return False

    val = 0
    now_c = 7
    for i in range(3, -1, -1):
        val += convertNum(tmp[i][now_c])
        now_c -= 1
    if val + 4 != 26:
        return False

    val = 0
    now_c = 1

    for i in range(1, 5):
        val += convertNum(tmp[i][now_c])
        now_c += 1
    if val + 4 != 26:
        return False

    val = 0
    now_c = 4
    for i in range(4, 0, -1):
        val += convertNum(tmp[i][now_c])
        now_c += 1
    if val + 4 != 26:
        return False

    val = 0
    for i in range(7, 0, -2):
        val += convertNum(tmp[1][i])
    if val + 4 != 26:
        return False

    ret = ""
    for i in tmp:
        ret += "".join(i)
    answer.append(ret)

    return True


def apply_perm(combi):
    tmp = grid
    for idx, pos in enumerate(x_pos):
        tmp[pos[0]][pos[1]] = str(convertAlpha(combi[idx]))
    return tmp


def dfs(pick):
    if pick == x_cnt:
        if solution(apply_perm(combi)):
            for i in range(0, 45, 9):
                print(answer[0][i : i + 9])
            exit(0)
        return
    for i in range(12):
        if not visited[i]:
            visited[i] = True
            combi.append(i)
            dfs(pick + 1)
            visited[i] = False
            combi.pop()


N = 5
grid = []

for i in range(5):
    data = input()
    grid.append(list(data))
x_cnt = 0
x_pos = []
visited = [False] * 12
answer = []


for i in range(5):
    for j in range(9):
        if grid[i][j] == "x":
            x_cnt += 1
            x_pos.append((i, j))
        if grid[i][j] != "x" and grid[i][j] != ".":
            visited[convertNum(grid[i][j])] = True

combi = []
dfs(0)
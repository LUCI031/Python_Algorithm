# def win_chk(sy, sx, paths, game):
#     OX = game[sy][sx]
#     x_win = 0
#     o_win = 0

#     if OX == '.':
#         return x_win, o_win

#     for path in paths:
#         dy, dx, cnt = sy, sx, 1

#         while 0 <= dy + path[0] < 3 and 0 <= dx + path[1] < 3 and OX == game[dy + path[0]][dx + path[1]]:
#             cnt += 1
#             dy += path[0]
#             dx += path[1]

#         if cnt == 3:
#             if OX == 'O':
#                 o_win += 1
#             elif OX == 'X':
#                 x_win += 1

#     return x_win, o_win

# start_points = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]]
# paths = [
#     [[0, 1], [1, 1], [1, 0]],
#     [[1, 0]],
#     [[1, -1], [1, 0]],
#     [[0, 1]],
#     [[0, 1]]
# ]

# while True:
#     inp = input()
    
#     if inp == 'end':
#         break

#     game = []
#     tmp = []
    
#     for i in range(1, 10):
#         tmp.append(inp[i - 1])
#         if (i % 3 == 0):
#             game.append(tmp)
#             tmp = []

#     x_win = 0
#     o_win = 0

#     for index in range(len(start_points)):
#         dx_win, do_win = win_chk(start_points[index][0], start_points[index][1], paths[index], game)
#         x_win += dx_win
#         o_win += do_win
    
#     x_cnt = inp.count('X')
#     o_cnt = inp.count('O')
#     d_cnt = inp.count('.')

#     if x_win > o_win and x_cnt == o_cnt + 1:
#         print('valid')
#         continue

#     if o_win > x_win and x_cnt == o_cnt:
#         print('valid')
#         continue

#     if o_win == x_win == 0 and d_cnt == 0 and x_cnt == o_cnt + 1:
#         print('valid')
#         continue

#     print('invalid')

while True:
    s = input()
    if s == "end":
        break
    
    s_count = s.count("X")
    x_count = s.count("O")

    sub = s_count - x_count

    if 0 > sub or sub > 2:
        print("invalid")
        continue
    
    if s_count + x_count == 9:
        print("valid")
        continue

    bingo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    boolean = False

    for i in bingo:
        x, y, z = i[0]-1, i[1]-1, i[2]-1

        if s[x] == ".":
            continue

        if s[x] == s[y] == s[z]:
            if s[x] == "O" and s_count == x_count:
                boolean = True
                break
            
            if s[x] == "X" and s_count == x_count+1:
                boolean = True
                break
                
    
    if boolean == True:
        print("valid")
    else:
        print("invalid")
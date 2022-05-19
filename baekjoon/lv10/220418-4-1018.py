import sys
input=sys.stdin.readline

M, N = map(int,input().split()) # M 세로 N 가로
board = []
result = []
for i in range(M):
    board.append(list(input()))
    board[i].remove('\n')
    
for j in range(M-7):
    for k in range(N-7):
        first_W = 0
        first_B = 0
        for l in range(j,j+8):
            for o in range(k,k+8): 
                if (l+o)%2 == 0: #짝수 홀수 확인 (0,1 0,2 0,3 이 지점 확인)
                    if board[l][o] != 'W':
                        first_W += 1
                    if board[l][o] != 'B':
                        first_B += 1
                else:
                    if board[l][o] != 'B':
                        first_W += 1
                    if board[l][o] != 'W':
                        first_B += 1
        result.append(first_W)
        result.append(first_B)
print(min(result))

import sys
input = sys.stdin.readline

words = input().strip()
ans = ''
cnt = 0
lst = []
for i in words:
    if i == '.':
        if lst:
            a = 'AAAA' * (len(lst)//4)
            ans += a
            if len(lst)%4 == 2:
                ans += 'BB'
            elif len(lst)%4 == 1 or len(lst)%4 == 3:
                print(-1)
                exit()
        lst = []
        ans += '.'
    else:
        lst += i

a = 'AAAA' * (len(lst)//4)
ans += a
if len(lst)%4 == 2:
    ans += 'BB'
elif len(lst)%4 == 1 or len(lst)%4 == 3:
    print(-1)
    exit()

print(ans)

# 모범 답안
# board = input()

# board = board.replace("XXXX", "AAAA")
# board = board.replace("XX", "BB")

# if 'X' in board:
#     print(-1)
    
# else:
#     print(board)

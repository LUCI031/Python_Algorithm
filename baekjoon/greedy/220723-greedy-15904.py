import sys
input = sys.stdin.readline

words = input().strip()
ans = 'UCPC'
cnt = 0
for word in words:
    if word == ans[cnt]:
        cnt += 1
    if cnt > 3:
        print('I love UCPC')
        exit()

print('I hate UCPC')
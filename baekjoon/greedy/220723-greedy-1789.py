import sys
input = sys.stdin.readline

answer = 0
cnt = 0
S = int(input())

for i in range(1,S+1):
    answer += i
    cnt += 1
    if answer > S:
        cnt -= 1
        break

print(cnt)
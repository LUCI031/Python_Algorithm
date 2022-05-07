# 백준 5622 다이얼
# 내 답
import sys
input=sys.stdin.readline

dial = list(input().upper())
timer = 0

for i in dial:
    num = ord(i)
    if 65 <= num <= 67: #2
        timer += 3
    elif 68 <= num <= 70: #3
        timer += 4
    elif 71 <= num <= 73: #4
        timer += 5
    elif 74 <= num <= 76: #5
        timer += 6
    elif 77 <= num <= 79: #6
        timer += 7
    elif 80 <= num <= 83: #7 4
        timer += 8
    elif 84 <= num <= 86: #8
        timer += 9
    elif 87 <= num <= 90: #9 4
        timer += 10
print(timer)

# 모범 답안

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

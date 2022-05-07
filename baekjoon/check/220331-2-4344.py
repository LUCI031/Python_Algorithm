#백준 4344
#평균 퍼센테이지 표현
#내가 쓴 답
import sys
input=sys.stdin.readline

c = int(input())
sums = 0
result = 0
scores = []
for _ in range(c):
    nums = list(map(int, input().split()))
    scores.append(nums)
    
for i in range(len(scores)):
    point = scores[i]
    for i in range(1, len(point)):
        sums = sums + point[i]
    avg = sums/point[0]
    for i in range(1, len(point)):
        if point[i] > avg:
            result += 1
    
    print('{:.3f}%'.format(result/point[0]*100))
    sums = 0
    result = 0

# 모범답안
num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')
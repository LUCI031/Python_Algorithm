#백준 8958 OX 퀴즈
#내가 쓴 답
# import sys
# input=sys.stdin.readline

n = int(input())
cnt1 = 0
cnt2 = 0
answer = []
for i in range(0,n):
    answer.append(list(input()))
    answer[i].remove('\n')

for i in range(0,len(answer)):
    tester = answer[i]
    for i in range(0,len(tester)):
        if tester[i] == 'O':
            cnt1 += 1
            cnt2 = cnt2 + cnt1
        else:
            cnt1 = 0
    print(cnt2)
    cnt2=0
    cnt1=0
#모범답안
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)
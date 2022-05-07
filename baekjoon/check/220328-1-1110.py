# 백준 1110
#내가 푼 방식

# import sys
# input=sys.stdin.readline
# count = 0
# new1 = int(input())
# if new1 < 10:
#      preNum = new1
#      newNum = new1
# else: 
#     preNum = new1%10
#     newNum = new1//10 + new1%10
#     newNum = preNum*10 + newNum%10
#     count += 1
# while True:
#     preNum = newNum%10
#     newNum = newNum//10 + newNum%10
#     newNum = preNum*10 + newNum%10
#     count += 1
#     if new1 == newNum:
#         break       
# print(count)

# 모법답안
input_num = int(input())

num = input_num  # num 변수에 input_num을 지정
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if new_num == input_num :
        break
    num = new_num  # num 변수에 last_num을 지정 
print(cnt)
# 백준 2675 문자열 반복
# 내가 푼 방식
# import sys
# input=sys.stdin.readline

# S_arr = []
# R_arr = []
# T = int(input())

# for i in range(0, T):
#     R,S = map(str, input().split())
#     S = list(S)
#     R = int(R)
#     S_arr.append(S)
#     R_arr.append(R)

# for i in range(0, T):
#     S2 = list(S_arr[i])
#     R2 = int(R_arr[i])
#     for i in range(0, len(S2)):
#         print(S2[i]*R2,end='')
#     print('')

# 모범답안
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
import sys
input=sys.stdin.readline
N = int(input())
cnt = 1
room = 1

while N > room:
    room = room + (cnt*6)
    cnt += 1

print(cnt)
# 2~7 5/ 8~19 11/ 20~37 17/ 38~61
# 한단계 올라갈 때마다 6개 추가
# 아이디어는 몇개 떠올랐으나 구현 실패
# 답보고 제출
# 막판에 답 봤으나 자꾸 시간 초과되어 확인해보니
# cnt += 1 을 깜빡했음
    # y 층수 x 방 넘버 방 넘버 작은게 중요
# 1번방 다 차면 2번방 이런 식으로
# 아웃풋은 N번째 손님한테 배정되는 방번호
# T = 테스트 갯수
# H = 층 W = 방 N = 손님

    # 깨달음 전 for문으로 해결하려 함
    # while True:
    #     for j in range(1,Room+1):
    #         for i in range(1, Floor+1):
    #             if cnt == Guest:
    #                 if j < 10:
    #                     print(f"{Floor_num}0{j}")
    #                     break
    #                 else:
    #                     print(f"{Floor_num}{j}")
    #                     break
    #             else:
    #                 Floor_num += 1
    #                 cnt += 1
    #         Floor_num = 1
        
import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    h,w,n = list(map(int,input().split()))
    if n%h == 0:
        curr_f = h*100
        curr_r = n//h
    else:
        curr_f = (n%h)*100
        curr_r = n//h + 1
    print(curr_f+curr_r)

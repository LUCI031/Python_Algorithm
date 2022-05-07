#배운대로 풀었더니 시간 초과
#에라토스테네스 사용
#예외처리 (1 or N is Prime)
#N이 소수일 때 처리가 제대로 안되서 계속 고침
#결국 엄청 간단하게 풂
#설탕 문제 반대
import sys
input=sys.stdin.readline

N = int(input())
if N == 1:
    pass
for i in range(2,N+1):
    while N%i == 0:
        print(i)
        N = N//i
        if N < 0:
            break
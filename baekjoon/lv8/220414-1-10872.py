# for문으로 구현해보려다 포기하고 함수 만듦
import sys
input=sys.stdin.readline

N = int(input())

# def facto(n):
#     if n > 0:
#         return int(n*facto(n-1))
#     else:
#         return 1
    
# print(facto(N))

# for 문
result = 1
if N > 0:
    for i in range(1,N+1):
        result *= i
print(result)
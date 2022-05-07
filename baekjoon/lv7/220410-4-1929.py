# 그대로 했더니 시간 초과
# M, N = 1, M,N이 소수일 경우 등 추가
import sys
input=sys.stdin.readline

# def isPrime(m,n):
#     n += 1
#     prime = [True] * n
#     for i in range(2, int((n**0.5)+1)):
#         if prime[i]:
#             for j in range(2*i, n, i):
#                 prime[j] = False
#     for i in range (m, n):
#         if i > 1 and prime[i] == True:
#             print(i)

# M,N = map(int,input().split())
# if M == 1 or N == 1:
#     pass
# else:
    # isPrime(M,N)
    

x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1:
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)
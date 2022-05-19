import sys
input=sys.stdin.readline

# a층 b호 조건
# a-1층 1~b호 사람들 수의 합만큼 사람 필요
#빈집 없음 
# k층 n호 
# 0층부터 i=n

T = int(input())

for i in range(T):
    k = int(input()) #층
    n = int(input()) #호
    if k == 0:
        print(n)
    elif n == 1:
        print(1)
    else:
        k0 = [i for i in range(1,n+1)]

        for i in range(k):
            result = []
            for j in range(n):
                result.append(sum(k0[0:j+1]))
            k0 = result
            
        print(k0[-1])
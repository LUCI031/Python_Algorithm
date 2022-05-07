# 리스트 뽑고 큰 for문 만든건 좋았으나 
# for문이 3개 나와서 이상함 감지
# for문 if문 많이 나와 시간 초과, 횟수 줄일 방법 생각
# 중간에서부터 시작하는 법 찾기, 
# 그랬더니 틀렸다고 나와서 range 범위 3까지인거 2로 수정

import math
import sys
input=sys.stdin.readline

def isPrime(N):
    nums = [True]*(N+1)
    m = int(N ** 0.5)+1   
    if N == 1:
        pass
    else:
        for i in range(2,m):
            if nums[i]:
                for j in range(2*i, N+1, i):
                    nums[j] = False
    return [a for a in range(2,N+1) if nums[a] == True]


T = int(input())

for i in range(T):
    n = int(input())
    middle = math.floor(n/2)
    primes = isPrime(n)
    min_num = 0
    
    for j in range(middle,1,-1):
        if j in primes:
            if 2*j == n:
                min_num = j
                break
            elif n-j in primes:
                min_num = j
                break    
    print(f"{min_num} {n-min_num}")
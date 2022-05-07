# 소수 만드는 법 아니까 금방 품
import sys
input=sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False  
    return True

M = int(input())
N = int(input())
primes = []
cnt = 0
for i in range(M, N+1):
    if isPrime(i) == True:
        primes.append(i)
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])
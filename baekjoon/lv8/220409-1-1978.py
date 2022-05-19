#소수 찾기
# 식 찾느라 1차 고생, 함수 이해하느라 2차 고생
import sys
input=sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

for i in nums:
    if isPrime(i) == True:
        cnt += 1
print(cnt)
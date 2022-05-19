import math
import sys
input=sys.stdin.readline

N, K = map(int,input().split())

# print(math.comb(N,K))

# 다른 방법
def facto(a):
    if a == 0:
        return 1
    return a*facto(a-1)

print(facto(N)//(facto(K)*facto(N-K)))
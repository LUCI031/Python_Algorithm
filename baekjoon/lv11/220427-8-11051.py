import math
import sys
input=sys.stdin.readline

def facto(a):
    if a < 2:
        return 1
    else:
        return a*facto(a-1)

N,K = map(int,input().split())

print((facto(N)//(facto(K)*facto(N-K)))%10007)

# print(math.comb(N,K)%10007)
import math
import sys
input=sys.stdin.readline

T = int(input())

for i in range(T):
    x,y = map(int,input().split())
    print(int(x*y/math.gcd(x,y)))
import math
import sys
input=sys.stdin.readline

x,y = map(int,input().split())

print(math.gcd(x,y))
print(int(x*y/math.gcd(x,y)))
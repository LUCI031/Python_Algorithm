import sys
import math
input=sys.stdin.readline

R = int(input())

print(round(math.pi*(R**2), 6))
print('{:.6f}'.format(float((R**2)*2)))
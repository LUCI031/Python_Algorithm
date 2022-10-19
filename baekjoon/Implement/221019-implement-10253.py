import sys
from fractions import Fraction
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    while a != 1:
        c = b//a+1
        a=a*c-b
        b=b*c
        a,b = map(int,str(Fraction(a,b)).split('/'))
    print(b)
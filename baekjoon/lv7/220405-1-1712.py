import sys
input=sys.stdin.readline

A,B,C = map(int,input().split())
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)
    
#수학적인 사고 필요
#답 보고 품
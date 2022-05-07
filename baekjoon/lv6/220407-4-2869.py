#달팽이
# x = V/(A-B)
# V%A와 V%(A-B) 비교
# 반올림 사용
# V 이상이 되기 직전 단계를 계산하려다 실패
import math
import sys
input=sys.stdin.readline

A,B,V = map(int,input().split())
cnt = V//(A-B)
if V<=A == 0:
    print(1)
else: 
    print(math.ceil((V-B)/(A-B)))

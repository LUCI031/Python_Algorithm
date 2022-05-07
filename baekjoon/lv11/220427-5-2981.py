# https://stujune-to-devjune.tistory.com/40 풀이
# 1. 입력 받음
# 2. 모든 값들이 (나머지)*(값) -> A-B=M(i-j)
# 3. 뺀 값들의 최대 공약수 구함
# 4. 해당 최대 공약수의 모든 공약수 구함
import sys
import math
input=sys.stdin.readline

def div(x): # 공약수 리스트
    div_lst = [x]
    for i in range(2, int(x**(1/2)+1)):
        if x % i == 0:
            div_lst.append(i)
            if x // i != i:
                div_lst.append(x//i)
    div_lst.sort()       
    return div_lst

N = int(input())
lst = sorted([int(input()) for _ in range(N)])
new_lst = []

for j in range(N-1,0,-1):
    new_lst.append(lst[j]-lst[j-1])
new_lst.sort()

if len(new_lst) == 1:
    answer = new_lst[0]
else:
    answer = new_lst[0]
    for k in range(len(new_lst)):
        answer = math.gcd(answer, new_lst[k])

for g in div(answer):
    print(g, end=' ')
    
# print(new_lst)
# for k in new_lst:
#     for g in range(int(k**0.5+1)):
#         if g < g:
#             break
#         if k%g == 0:
#             result.append(g)
#             if k
    
# print(result)